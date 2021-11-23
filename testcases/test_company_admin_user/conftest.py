import pytest

from tpmain_api_test.data_template.base_data import Data, UserFromCreate
from tpmain_api_test.operators import CompanyAdminFactory, CompanyAdminOperator


class MyData(Data):
    test_company_admin = CompanyAdminFactory("test_company_admin", "admin")
    new_company_admin = CompanyAdminFactory("new_company_admin", "admin", is_single=False)
    test_company_admin_user = UserFromCreate("test_company_admin")


@pytest.fixture(scope="module")
def data(data):
    d = MyData(data)
    yield d


@pytest.fixture(scope="class")
def new_company_admin(data):
    company_admin: CompanyAdminOperator = data.new_company_admin
    yield company_admin
