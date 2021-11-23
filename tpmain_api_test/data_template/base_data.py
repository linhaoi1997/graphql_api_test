from graphql_api_object.base_operator.base_data import BaseData

from config import account, password
from tpmain_api_test import User
from tpmain_api_test.operators import *


class UserFromCreate:

    def __init__(self, operator_name):
        self.operator_name = operator_name

    def __get__(self, instance, owner):
        if not instance.__dict__.get(self.operator_name + "_client"):
            instance.__dict__[self.operator_name + "_client"] = getattr(instance, self.operator_name).client
        return instance.__dict__.get(self.operator_name + "_client")


class Data(BaseData):
    admin = User(account, password)
    company = CompanyFactory("company", "admin")

    def setup(self):
        company_: CompanyOperator = self.company
        company_.change_permissions(["平台"])

    root_department = RootDepartment("admin")

    department1 = DepartmentFactory("department1", "admin", parent="root_department")
    department2 = DepartmentFactory("department2", "admin", parent="root_department")

    role1 = RoleFactory("role1", "admin")
    role2 = RoleFactory("role2", "admin")

    company_admin = CompanyAdminFactory("company_admin", "admin")
    company_admin_user = UserFromCreate("company_admin")

    user1 = UserFactory("user1", "company_admin_user", role="role1", department="department1")
    user2 = UserFactory("user2", "company_admin_user", role="role2", department="department2")
    new_user = UserFactory("new_user", "company_admin_user", role="role1", department="department1", is_single=False)


if __name__ == '__main__':
    data = Data()
    try:
        print(data.create_all_resource())
        id1 = data.new_user.id
        id2 = data.new_user.id
        assert id1 != id2
    except Exception as e:
        data.company.delete()
        raise e
    finally:
        data.company.delete()
