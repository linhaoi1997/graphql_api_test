from graphqlapiobject.BaseOperator import BaseFactory
from .company_admin_operator import CompanyAdminOperator
from ...apis.Mutation_apis import CreateCompanyAdminUser
from ...apis.Query_apis import CompanyAdminUsers


class CompanyAdminFactory(BaseFactory):
    # 创建部分
    create_api = CreateCompanyAdminUser  # 创建调用的接口
    create_args = ["company.id"]  # 创建默认的参数,基本参数如company id
    # 查询部分
    query_api = CompanyAdminUsers  # 查询的列表接口

    query_path = "data"  # 返回结果中对应的列表路径
    query_field = "account"  # 路径下对应的查找的值
    query_value_path = "account"  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator = CompanyAdminOperator

    @classmethod
    def _query_from_list(cls, user, create_api, query_filter):
        info = super(CompanyAdminFactory, cls)._query_from_list(user, create_api, query_filter)
        info["password"] = create_api.result
        return info
