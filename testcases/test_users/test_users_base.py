from graphql_api_object.base_operator.base_test_cases_template import *
import allure

from tpmain_api_test.apis import Users
from tpmain_api_test.operators import UsersQueryOperator


@allure.feature("用户管理")
@allure.story("创建用户")
class TestCreateUser(CreateCasesTemplate):
    operator = "new_user"  # 要更新的对象
    assert_jmespath = [
        "account",
        "name",
        "company.id",
        "department.id",
        "role[*].id",
        "phone",
        "email",
        "desc",
        "isActive"
    ]  # 校验jmespath


@allure.feature("用户管理")
@allure.story("删除用户")
class TestDeleteUser(DeleteCasesTemplate):
    operator = "new_user"  # 要删除的对象


@allure.feature("用户管理")
@allure.story("查询用户")
class TestQueryFilterUsers(QueryFilterCasesTemplate):
    query: BaseQueryOperator = UsersQueryOperator
    user = "company_admin_user"

    filters_info = [
        {
            "filter_key": "department",
            "data": [
                {"filter_value": lambda x: [{"id": x.department1.id}], "value": ["user1"]},
                {"filter_value": lambda x: [{"id": x.department2.id}], "value": ["user2"]},
            ]
        },
        {
            "filter_key": "department",
            "data": [
                {"filter_value": lambda x: [{"id": x.department1.id}, {"id": x.department2.id}],
                 "value": ["user1", "user2"]},
            ]
        },
        {
            "filter_key": "role",
            "data": [
                {"filter_value": lambda x: [{"id": x.role1.id}], "value": ["user1"]},
                {"filter_value": lambda x: [{"id": x.role2.id}], "value": ["user2"]},
            ]
        },
    ]


@allure.feature("用户管理")
@allure.story("查询用户")
class TestQueryPagingUsers(QueryPagingCasesTemplate):
    query_api = Users
    user = "company_admin_user"
    resource: str = "new_user"  # base_data中的属性

    def make_query_args(self, data):
        return {"filter": {"company": {"id": getattr(data, "company").id}}}
