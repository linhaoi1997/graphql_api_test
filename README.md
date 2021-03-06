# 接口自动化实践

1. 项目背景
    
    公司后端技术采取的是 [graphql](https://graphql.org/) 来定义接口。每次项目开发之后，开发会先给出一份schema，前端根据这份schema去了解数据定义，schema先行，前端根据这份schema也有自己的mock技术，前后端并行开发
    
    采取微服务方式部署，graphql网关会把所有的微服务集合起来，暴露一个地址给前端调用
    
    一个graphql定义的请求体大概是这样的
    
    ```jsx
    {
      "operationName": "typeCompanies",
      "variables": {
        "filter": {
          "search": ""
        },
        "scenario": "COMPANY"
      },
      "query": "query typeCompanies($filter: CompanyFilter, $scenario: TypeCompaniesScenario) {\n  typeCompanies(filter: $filter, scenario: $scenario) {\n    data {\n      type {\n        id\n        name\n        __typename\n      }\n      companies {\n        ...companyFields\n        __typename\n      }\n      __typename\n    }\n    totalCount\n    __typename\n  }\n}\n\nfragment companyFields on Company {\n  id\n  name\n  county\n  address\n  uscc\n  contact\n  email\n  phone\n  province\n  city\n  type {\n    id\n    name\n    __typename\n  }\n  isMine\n  __typename\n}\n"
    }
    ```
    
    在query中，graphql定义了要传入的参数，和返回的值，其中返回的值可以进行按需查询
    
    ```jsx
    query  typeCompanies($filter:  CompanyFilter,  $scenario:  TypeCompaniesScenario)  {
        typeCompanies(filter:  $filter,  scenario:  $scenario)  {
            data  {
                type  {
                    id
                    name
                    __typename
                }
                companies  {
                    ...companyFields
                    __typename
                }
                __typename
            }
            totalCount
            __typename
        }
    }
    fragment  companyFields  on  Company  {
        id
        name
        county
        address
        uscc
        contact
        email
        phone
        province
        city
        type  {
            id
            name
            __typename
        }
        isMine
        __typename
    }
    ```
    
2. 解决难点
    1. 如何构建graphql的复杂query
    2. 如何进行数据的准备
    3. 对于重复用例如何复用代码，降低自动化测试的成本
3. 实现思路
    1. 期望可以使用命令自动生成api的model，对于query的按需查询，可以通过参数的形式快速指定查询所有字段还是只查询部分字段
    2. 期望可以使用简单的代码进行数据准备的定义
    3. 对于CRUD的测试用例，期望可以使用模版的形式进行复用，只需要配置可以进行测试用例的执行
4. 代码封装思路
    1. 通过命令及代码自动生成api model的代码
        
         通过调研，发现graphql对于python客户端的支持有几个库，通过对比，选定sgqlc这个库，主要因为这个库有以下优点
        
        1. 可以通过schema，使用命令的形式生成python代码，使用python定义了schema中的所有type，接口，input
        2. 可以使用python代码一步一步构建复杂的query，并发送请求
        
        但是通过这个库构建请求还是有些复杂，所以经过开发，又进行了一层封装，主要在sgqlc的基础上实现以下功能，最终代码使用如下
        
        1. 接口的快速定义
            
            通过继承基础接口快速实现接口的定义
            
            ```python
            class TypeCompanies(GraphqlQueryListAPi):
                api = Query.type_companies
            
            user = User("account","password")
            
            result = TypeCompanies(user).run(scenario= 'COMPANY',filter={}).result
            ```
            
        2. 接口参数的自动生成
            
            对于create这类复杂参数的接口，通过sgqlc生成的schema来实现参数的自动生成，并且支持修改重要的数据
            
            ```python
            class CreateCompany(GraphqlOperationAPi):
                api = Mutation.create_company
            
            user = User("account","password")
            result = CreateCompany(user).auto_run(
                {
                    "type.id":10
                }
            ).result
            ```
            
        3. 接口模型代码的自动生成
            
            通过importlib，动态引入schema类，一键自动创建所有的api模型（根据名称分配接口类型）
            
            ```python
            gen("schema.platform_schema", "apis")
            ```
            
        4. 根据后端接口规范进行不同类型接口的封装（增删查改）
    2. 数据的准备
        
        数据准备难点在于创建的资源可能是依赖于其他资源的
        
        现在想到的解决方案就是使用一个类去定义一份数据模版，把所有的资源都放到这个数据模版中，每个资源如果创建要依赖其他资源，就去指定属性，从数据模版中获取
        
        大部分的业务的资源创建都可以归结为 创建→查询，每个资源都有自己的业务（对应接口的update）和删除（接口的delete）
        
        最终实现代码如下
        
        ```python
        class Data(BaseData):
            admin = User(account, password)
            company = CompanyFactory("company", "admin")
        
            def setup(self):
                company_: CompanyOperator = self.company
                company_.change_permissions(["平台"])
        
            root_department = RootDepartment("admin")
        
            department1 = DepartmentFactory("department1", "admin", parent="root_department")
            department2 = DepartmentFactory("department2", "admin", parent="root_department")
        
            role1 = RoleFactory("role1", "admin")
            role2 = RoleFactory("role2", "admin")
        
            company_admin = CompanyAdminFactory("company_admin", "admin")
            company_admin_user = UserFromCreate("company_admin")
        
            user1 = UserFactory("user1", "company_admin_user", role="role1", department="department1")
            user2 = UserFactory("user2", "company_admin_user", role="role2", department="department2")
        ```
        
        每一个Factory都继承自BaseFactory，实现了 `__get__` 方法，所以数据模版中的每份资源都不会立刻被创建，只有调用的时候才会一层一层创建资源
        
        可以对数据模版进行自由的扩展，支持实例化数据模版的时候传入已经实例化的data，会继承现有的数据，扩展新的数据。
        
        这样的缺点也很明显就是如果资源太多，代码就会变得非常多，暂时没有想到好的解决办法
        
        每个资源对应一个业务模型，每个业务模型要实现自己对应的操作
        
        ```python
        class UserOperator(BaseOperator):
            update_api = UpdateUser
            delete_api = DeleteUsers
        
            def delete(self):
                return self.delete_api(self.user).run(
                    input={
                        "ids": [self.id]
                    }
                )
        
            def reset_password(self):
                return ResetPassword(self.user).run(
                    input={"userIDs": [self.id]},
                    scenario="NORMAL_USER"
                ).c("[0].password")
        
            @property
            def _role_input(self):
                return [{"id": i["id"] for i in self.info["role"]}]
        
            def update_part(self, kwargs):
                kwargs["id"] = self.id
                if not kwargs.get("role"):
                    kwargs["role"] = self._role_input
                return self.update_api(self.user).run(
                    **{"input": kwargs}
                )
        
            @property
            def client(self):
                return User(self.info["account"], self.info["password"])
        
            def update_name(self, name):
                return self.update_part({"name": name})
        
            def update_department(self, department):
                return self.update_part({"department": {"id": department.id}})
        
            def update_role(self, role: list):
                return self.update_part({"role": [{"id": r.id} for r in role]})
        
            def active(self):
                return self.update_part({"isActive": True})
        
            def forbidden(self):
                return self.update_part({"isActive": False})
        ```
        
    3. 测试用例模版，
        
        对于同类型的用例，使用模版配置的方式快速填写
        
        创建：创建的资源可以查询到，创建的所有信息正常保存
        
        查询：列表查询，分页，筛选
        
        删除：删除成功，查询不到该资源
        
        基于此写了测试用例的模版基类，所有测试用例类继承，最终实现代码如下
        
        ```python
        @allure.feature("企业管理")
        @allure.story("创建企业")
        class TestCreateCompany(CreateCasesTemplate):
            operator = "new_company"  # 要更新的对象
            assert_jmespath = [
                "address",
                "city",
                "contact",
                "county",
                "email",
                "name",
                "phone",
                "province",
                "uscc"
            ]  # 校验jmespath
        
        @allure.feature("企业管理")
        @allure.story("删除企业")
        class TestDeleteCompany(DeleteCasesTemplate):
            operator = "test_company"  # 要删除的对象
        
        @allure.feature("企业管理")
        @allure.story("查询企业")
        class TestQueryCompanies(QueryFilterCasesTemplate):
            query = CompanyQueryOperator
            user = "admin"
        
            filters_info = [
                {
                    "filter_key": "search",
                    "data": [
                        {"filter_value": lambda x: x.company1.info["name"][:-1], "value": ["company1"]},
                        {"filter_value": lambda x: x.company2.info["name"][:-1], "value": ["company2"]},
                    ]
                }
            ]
        ```
        
    
    4. 不同项目的依赖解决方案
    
    公司的业务是多服务的形式，有时一个服务的接口要依赖其他app的接口，那么可能A项目写的接口测试依赖于B接口测试写的接口和数据
    
    这种情况采取打包的方式，将所有的apis，业务对象，数据模版使用poetry打成python包，如果其他项目需要依赖，那么pip  install就可以
    

结尾

以上就是基于graphql的接口自动化实践，可以快速对已有接口进行CRUD的测试用例，并且对其他测试用例进行扩展。

不足之处的思考：

1. 资源多的情况下数据模版代码会变得很长，需要优化
2. 部分配置项还略显臃肿，部分配置不够灵活
3. 暂时想不到加入数据驱动的优化
4. 看是否可以结合httprunner，是否可以规范化测试的步骤