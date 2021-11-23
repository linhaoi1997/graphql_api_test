import allure
import pytest
from graphql_api_object import fake

from tpmain_api_test import User


@allure.feature("企业管理")
@allure.story("企业管理员业务")
class TestCompanyAdminUser:

    @allure.title("更新名字")
    def test1(self, new_company_admin):
        new_name = fake.name
        new_company_admin.update_name(new_name)
        assert new_company_admin["name"] == new_name

    @allure.title("账号可以直接登录")
    def test2(self, new_company_admin):
        assert new_company_admin.client

    @allure.title("初始权限")
    def test3(self, new_company_admin):
        assert "平台" in new_company_admin.permissions

    @allure.title("重置密码登录")
    def test4(self, new_company_admin):
        new_password = new_company_admin.reset_password()
        with allure.step("使用旧密码无法登陆"):
            with pytest.raises(Exception):
                assert new_company_admin.client
        with allure.step("使用新密码可以登陆"):
            User(new_company_admin.info["account"], new_password)
