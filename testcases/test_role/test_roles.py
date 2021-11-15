from graphqlapiobject.BaseOperator.base_test_cases_template import *
import allure
from testcases.data import Data
from tpmain_api_test import User
from tpmain_api_test.define_permissions import PlatformMenuPermission, DataPermission
from tpmain_api_test.operators import RoleFactory, RoleQueryOperator


class PlatformRoleFactory(RoleFactory):
    permission_info = {
        PlatformMenuPermission.my_apps: DataPermission.ALL,
        PlatformMenuPermission.company_account_manage: DataPermission.OWN
    }


class MyData(Data):
    new_role = RoleFactory(
        "new_role", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
        ],
        query_filter=[],
        is_single=False
    )

    special_role = RoleFactory(
        "special_role", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
        ],
        query_filter=[]
    )


@pytest.fixture(scope="module")
def data(data):
    yield MyData(data)


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
@allure.story("更新角色")
class TestUpdateRole(UpdateCasesTemplate):
    create_factory: Type[BaseFactory] = PlatformRoleFactory  # 创建工厂
    operator = "new_role"  # 要更新的对象
    update_args: List = [
        {"key": "company.id", "attr_name": "company", "func": None}
    ]  # 更新的参数
    assert_jmespath: List[str or List[str]] = [
        "desc",
        "name",
        ["permissions[].permission.id", "permissions[].id"]
    ]  # 校验jmespath
    users: List[User] = ["company_admin_user", "admin"]


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
    query: BaseQueryOperator = RoleQueryOperator
    user = "company_admin_user"
    resource: str = "new_role"  # base_data中的属性
    company = "company"
