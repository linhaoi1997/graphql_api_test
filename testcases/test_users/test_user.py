import allure
import pytest
from assert_methods import list_equal
from graphql_api_object import fake

from tpmain_api_test import User
from hamcrest import assert_that


@allure.feature("用户管理")
@allure.story("用户业务")
class TestUser:

    @allure.title("禁止用户登录")
    def test1(self, new_user):
        new_user.forbidden()
        with pytest.raises(Exception):
            assert new_user.client

    @allure.title("修改用户名称")
    def test2(self, new_user):
        new_name = fake.name
        new_user.update_name(new_name)
        assert new_user["name"] == new_name

    @allure.title("启动用户登录")
    def test3(self, new_user):
        new_user.active()
        assert new_user.client

    @allure.title("重置用户密码")
    def test4(self, new_user):
        new_password = new_user.reset_password()
        assert User(new_user.info["account"], new_password)

    @allure.title("修改用户角色")
    def test5(self, new_user, data):
        new_user.update_role([data.role2, data.role1])
        assert_that(
            [data.role2.id, data.role1.id], list_equal([i["id"] for i in new_user["role"]])
        )

    @allure.title("修改用户部门")
    def test6(self, new_user, data):
        new_user.update_department(data.department2)
        assert data.department2.id == new_user["department"]["id"]
