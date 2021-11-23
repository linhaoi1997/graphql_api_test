from tpmain_api_test.operators import UserOperator
import pytest


@pytest.fixture(scope="class")
def new_user(data):
    user: UserOperator = data.new_user
    yield user
