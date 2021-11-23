import logging

import pytest

from tpmain_api_test.data_template.base_data import Data, UserFromCreate
from tpmain_api_test.operators import CompanyFactory, CompanyAdminFactory


class MyData(Data):
    new_company = CompanyFactory("new_company", "admin")
    company1 = CompanyFactory("company1", "admin")
    company2 = CompanyFactory("company2", "admin")
    test_company = CompanyFactory("test_company", "admin")

    test_company_admin = CompanyAdminFactory("test_company_admin", "admin", company="test_company")
    test_company_admin_user = UserFromCreate("test_company_admin")


@pytest.fixture(scope="module")
def data(data):
    logging.info(data.company.id)
    d = MyData(data)
    company_ = d.test_company
    company_.change_permissions(["平台"])
    yield d
    d.company1.delete()
    d.company2.delete()
    d.test_company.delete()


@pytest.fixture(scope="function", autouse=True)
def clear_company(data):
    data.__dict__["test_company"].delete()
