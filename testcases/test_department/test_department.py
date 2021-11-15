from jmespath import search
from graphqlapiobject.BaseOperator.base_test_cases_template import *
import allure
from testcases.data import Data
from tpmain_api_test.operators import DepartmentFactory


class MyData(Data):
    new_department = DepartmentFactory(
        "new_department", "admin",
        kwargs=[
            {"key": "parent.id", "attr_name": "root_department", "func": None}
        ],
        query_filter=[],
        is_single=False
    )


@pytest.fixture(scope="module")
def data(data):
    yield MyData(data)


@allure.feature("部门管理")
@allure.story("新建部门")
class TestCreateDepartment:

    @allure.title("测试创建部门")
    def test(self, data):
        new_department = data.new_department
        assert new_department.info["parent"] == search("input.parent.id", new_department.variables)
        assert new_department.info["name"] == search("input.name", new_department.variables)


@allure.feature("部门管理")
@allure.story("更新部门")
class TestUpdateDepartment:

    @allure.title("测试更新部门")
    def test(self, data):
        new_department = data.new_department
        update = new_department.update_all(
            {
                "id": new_department.id,
                "parent.id": data.department1.id,
            }
        )
        for detail in new_department.detail():
            assert detail["parent"] == search("input.parent.id", update.variables)
            assert detail["name"] == search("input.name", update.variables)


@allure.feature("部门管理")
@allure.story("删除部门")
class TestDeleteDepartment:

    @allure.title("测试删除部门")
    def test(self, data):
        new_department = data.new_department
        new_department.delete()
        with pytest.raises(AssertionError):
            list(new_department.detail())
