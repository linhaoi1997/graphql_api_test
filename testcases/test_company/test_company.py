import allure
import pytest
from graphql_api_object import fake

from tpmain_api_test.operators import CompanyOperator


@pytest.fixture(scope="class")
def new_company(data):
    company: CompanyOperator = data.new_company
    yield company


@allure.feature("企业管理")
@allure.story("企业业务")
class TestCompany:

    @allure.title("修改公司name")
    def test1(self, new_company):
        new_name = fake.name
        new_company.update_name(new_name)
        assert new_company["name"] == new_name

    @allure.title("修改公司type")
    def test2(self, new_company):
        new_company._query_list.set("data.companies.__fields__")
        new_company.update_type(7)
        assert new_company["type"]["id"] == "7"

    @allure.title("修改企业信用代码")
    def test3(self, new_company):
        new_uscc = fake.name
        new_company.update_uscc(new_uscc)
        assert new_company["uscc"] == new_uscc

    @allure.title("添加企业app")
    def test4(self, new_company):
        apps = ["销售管理", "客户管理"]
        new_company.add_apps(apps)
        for app in apps:
            assert app in new_company.apps

    @allure.title("添加企业权限")
    def test5(self, new_company):
        permissions = ["用户管理", "角色管理"]
        new_company.change_permissions(permissions)
        for permission in permissions:
            assert permission in new_company.permissions
