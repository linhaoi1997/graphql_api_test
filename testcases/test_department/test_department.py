import allure
from graphql_api_object import fake


@allure.feature("部门管理")
@allure.story("部门业务")
class TestDepartment:

    @allure.title("部门名称是否已存在:不存在")
    def test1(self, new_department):
        assert not new_department.name_exists(fake.name)

    @allure.title("部门名称是否已存在:存在")
    def test1(self, new_department):
        assert new_department.name_exists(new_department.info["name"])

    @allure.title("部门名称是否已存在--带上自己id")
    def test3(self, new_department):
        assert not new_department.name_exists_with_id(new_department.info["name"])
