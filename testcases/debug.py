from config import account, password
from tpmain_api_test import User
import pytest
from tpmain_api_test.operators.company.company_factory import CompanyFactory
from tpmain_api_test.operators.company.company_operator import CompanyOperator
from tpmain_api_test.operators.department.department_factory import DepartmentFactory, RootDepartment
from tpmain_api_test.operators.role.role_factory import RoleFactory
from tpmain_api_test.operators.company_admin.company_admin_factory import CompanyAdminFactory
from tpmain_api_test.operators.user.user_factory import UserFactory

from graphqlapiobject.BaseOperator.base_data import BaseData
from graphqlapiobject.BaseOperator.base_factory import IdDictBuilder


class Data(BaseData):
    admin = User(account, password)
    company = CompanyFactory("company", "admin", [], [], is_single=True, filter_has_company=False)

    root_department = RootDepartment("admin")

    department1 = DepartmentFactory(
        "department1", "admin",
        kwargs=[
            {"key": "parent.id", "attr_name": "root_department", "func": None}
        ],
        query_filter=[],
        is_single=True
    )
    role1 = RoleFactory(
        "role1", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
        ],
        query_filter=[],
        is_single=True
    )
    company_admin = CompanyAdminFactory(
        "company_admin", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
        ],
        query_filter=[
            {"key": "companyIDs", "attr_name": "company", "func": IdDictBuilder.id_to_list},
        ],
        is_single=True,
        filter_has_company=False
    )

    @property
    def company_admin_user(self):
        client = self.company_admin.client
        print(client)
        return client

    user1 = UserFactory(
        "user1",
        "company_admin_user",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
            {"key": "department.id", "attr_name": "department1", "func": None},
            {"key": "role", "attr_name": "role1", "func": IdDictBuilder.id_to_dict_list},
        ],
        query_filter=[],
        is_single=True,
    )


@pytest.fixture(scope="function")
def data():
    d = Data()
    yield d
    d.company.delete()


class TestDebug:

    def test1(self):
        c = CompanyFactory.new(user, {})
        print(c)
        print(c.info)
        print(c.id)

    def test2(self, data):
        print(data.company.id)
        # company: CompanyOperator = data.company
        # company.change_permissions(["平台"])
        print(data.department1.info)
