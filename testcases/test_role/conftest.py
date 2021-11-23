import pytest

from tpmain_api_test.data_template.base_data import Data
from tpmain_api_test.define_permissions import PlatformMenuPermission, DataPermission
from tpmain_api_test.operators import RoleFactory, RoleOperator


class PlatformRoleFactory(RoleFactory):
    permission_info = {
        PlatformMenuPermission.company_account_manage: DataPermission.OWN
    }


class MyData(Data):
    new_role = PlatformRoleFactory("new_role", "company_admin_user", is_single=False)
    special_role = RoleFactory("special_role", "company_admin_user")


@pytest.fixture(scope="module")
def data(data):
    yield MyData(data)


@pytest.fixture(scope="class")
def new_role(data):
    role: RoleOperator = data.new_role
    yield role
