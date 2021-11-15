import logging

from tpmain_api_test.operators import CompanyOperator
from testcases.data import Data
import pytest


@pytest.fixture(scope="session", autouse=True)
def data():
    data = Data()
    logging.info("创建公司")
    logging.info(data.company.info)
    company: CompanyOperator = data.company
    yield data
    company.delete()
