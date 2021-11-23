import pytest

from tpmain_api_test.data_template.base_data import Data
from tpmain_api_test.operators import DepartmentFactory, DepartmentOperator


class MyData(Data):
    new_department = DepartmentFactory("new_department", "admin", is_single=False)


@pytest.fixture(scope="module")
def data(data):
    yield MyData(data)


@pytest.fixture(scope="class")
def new_department(data):
    department: DepartmentOperator = data.new_department
    yield department
