from graphqlapiobject import IdDictBuilder

from graphqlapiobject.BaseOperator.base_test_cases_template import *
import allure

from tpmain_api_test import User
from tpmain_api_test.operators import UserFactory, UsersQueryOperator


@allure.feature("用户管理")
@allure.story("创建用户")
class TestCreateUser(CreateCasesTemplate):
    operator = "user1"  # 要更新的对象
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
@allure.story("更新用户")
class TestUpdateUser(UpdateCasesTemplate):
    create_factory: Type[BaseFactory] = UserFactory  # 创建工厂
    operator = "user1"  # 要更新的对象
    update_args: List = [
        {"key": "department.id", "attr_name": "department2", "func": None},
        {"key": "role", "attr_name": "role2", "func": IdDictBuilder.id_to_dict_list},
    ]  # 更新的参数
    assert_jmespath: List[str or List[str]] = [
        "name",
        "department.id",
        "role[*].id",
        "phone",
        "email",
        "desc",
        "isActive"
    ]  # 校验jmespath
    users: List[User] = ["company_admin_user", "admin"]


@allure.feature("用户管理")
@allure.story("删除用户")
class TestDeleteUser(DeleteCasesTemplate):
    operator = "user1"  # 要删除的对象


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
    query: BaseQueryOperator = UsersQueryOperator
    user = "company_admin_user"
    resource: str = "new_user"  # base_data中的属性
