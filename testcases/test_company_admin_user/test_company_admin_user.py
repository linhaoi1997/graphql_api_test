from graphqlapiobject import IdDictBuilder
from graphqlapiobject.BaseOperator.base_test_cases_template import *
import allure

from testcases.data import Data, UserFromCreate
from tpmain_api_test import User
from tpmain_api_test.operators import CompanyAdminFactory, \
    CompanyAdminQueryOperator, CompanyAdminOperator


class MyData(Data):
    test_company_admin = CompanyAdminFactory(
        "test_company_admin", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
        ],
        query_filter=[
            {"key": "companyIDs", "attr_name": "company", "func": IdDictBuilder.id_to_list},
        ],
        is_single=True,
        filter_has_company=False
    )
    new_company_admin = CompanyAdminFactory(
        "new_company_admin", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "company", "func": None},
        ],
        query_filter=[
            {"key": "companyIDs", "attr_name": "company", "func": IdDictBuilder.id_to_list},
        ],
        is_single=False,
        filter_has_company=False
    )
    test_company_admin_user = UserFromCreate("test_company_admin")


@pytest.fixture(scope="module")
def data(data):
    d = MyData(data)
    yield d


@allure.feature("企业管理")
@allure.story("创建企业管理员")
class TestCreateCompanyAdminUser(CreateCasesTemplate):
    operator = "new_company_admin"  # 要更新的对象
    assert_jmespath = [
        "account",
        "company.id",
        "email",
        "name",
        "phone",
    ]  # 校验jmespath


@allure.feature("企业管理")
@allure.story("更新企业管理员")
class TestUpdateCompanyAdminUser(UpdateCasesTemplate):
    create_factory: Type[BaseFactory] = CompanyAdminFactory  # 创建工厂
    operator = "new_company_admin"  # 要更新的对象
    update_args: List = []  # 更新的参数
    assert_jmespath: List[str or List[str]] = [
        "email",
        "name",
        "phone",
    ]  # 校验jmespath
    users: List[str] = ["admin"]

    @allure.title("更新管理员密码")
    def test_reset(self, data):
        operator: CompanyAdminOperator = data.new_company_admin
        new_password = operator.reset_password().capture("data.resetPassword[0].password")
        assert User(operator.info["account"], new_password)


@allure.feature("企业管理")
@allure.story("删除企业管理员")
class TestDeleteCompanyAdminUser(DeleteCasesTemplate):
    operator = "new_company_admin"  # 要删除的对象


@allure.feature("企业管理")
@allure.story("分页企业管理员")
class TestQueryCompanyAdminUsers(QueryPagingCasesTemplate):
    query: BaseQueryOperator = CompanyAdminQueryOperator
    user = "admin"
    resource: str = "company_admin_user"  # base_data中的属性
    company = "company"
