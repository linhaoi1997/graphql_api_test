from graphql_api_object.base_operator.base_test_cases_template import *
import allure
from tpmain_api_test.apis import RoleList
from tpmain_api_test.operators import RoleQueryOperator


@allure.feature("角色管理")
@allure.story("创建角色")
class TestCreateRole(CreateCasesTemplate):
    operator = "new_role"  # 要更新的对象
    assert_jmespath = [
        "desc",
        "name",
        ["permissions[].permission.id", "permissions[].id"]
    ]  # 校验jmespath


@allure.feature("角色管理")
@allure.story("删除角色")
class TestDeleteRole(DeleteCasesTemplate):
    operator = "new_role"  # 要删除的对象


@allure.feature("角色管理")
@allure.story("查询角色")
class TestQueryFiltersRoles(QueryFilterCasesTemplate):
    query: BaseQueryOperator = RoleQueryOperator
    user = "company_admin_user"
    company = "company"

    filters_info = [
        {
            "filter_key": "search",
            "data": [
                {"filter_value": lambda x: x.role1.info["name"][:-1], "value": ["role1"]},
                {"filter_value": lambda x: x.role2.info["name"][:-1], "value": ["role2"]},
            ]
        }
    ]


@allure.feature("角色管理")
@allure.story("查询角色")
class TestQueryPagingRoles(QueryPagingCasesTemplate):
    query_api = RoleList
    user = "company_admin_user"
    resource: str = "new_role"  # base_data中的属性
