from config import account, password
from tpmain_api_test import User
from tpmain_api_test.operators import *

from graphqlapiobject.BaseOperator.base_data import BaseData
from graphqlapiobject.BaseOperator.base_factory import IdDictBuilder


class UserFromCreate:

    def __init__(self, operator_name):
        self.operator_name = operator_name

    def __get__(self, instance, owner):
        if not instance.__dict__.get(self.operator_name + "_client"):
            instance.__dict__[self.operator_name + "_client"] = getattr(instance, self.operator_name).client
        return instance.__dict__.get(self.operator_name + "_client")


class Data(BaseData):
    admin = User(account, password)
    company = CompanyFactory("company", "admin", [], [], is_single=True, filter_has_company=False)

    def setup(self):
        company_: CompanyOperator = self.company
        company_.change_permissions(["平台"])

    root_department = RootDepartment("admin")

    department1 = DepartmentFactory(
        "department1", "admin",
        kwargs=[
            {"key": "parent.id", "attr_name": "root_department", "func": None}
        ],
        query_filter=[],
        is_single=True
    )

    department2 = DepartmentFactory(
        "department2", "admin",
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
    )
    role2 = RoleFactory(
        "role2", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
        ],
        query_filter=[],
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

    company_admin_user = UserFromCreate("company_admin")

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

    user2 = UserFactory(
        "user2",
        "company_admin_user",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
            {"key": "department.id", "attr_name": "department2", "func": None},
            {"key": "role", "attr_name": "role2", "func": IdDictBuilder.id_to_dict_list},
        ],
        query_filter=[],
        is_single=True,
    )

    new_user = UserFactory(
        "new_user",
        "company_admin_user",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
            {"key": "department.id", "attr_name": "department1", "func": None},
            {"key": "role", "attr_name": "role1", "func": IdDictBuilder.id_to_dict_list},
        ],
        query_filter=[],
        is_single=False,
    )
