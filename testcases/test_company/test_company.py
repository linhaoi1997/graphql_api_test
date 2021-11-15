from graphqlapiobject import IdDictBuilder
from graphqlapiobject.BaseOperator.base_test_cases_template import *
import allure

from testcases.data import Data, UserFromCreate
from tpmain_api_test.operators import CompanyFactory, CompanyQueryOperator, CompanyAdminFactory


class MyData(Data):
    new_company = CompanyFactory("new_company", "admin", [], [], is_single=False, filter_has_company=False)
    company1 = CompanyFactory("company1", "admin", [], [], is_single=True, filter_has_company=False)
    company2 = CompanyFactory("company2", "admin", [], [], is_single=True, filter_has_company=False)
    test_company = CompanyFactory("test_company", "admin", [], [], is_single=True, filter_has_company=False)

    test_company_admin = CompanyAdminFactory(
        "test_company_admin", "admin",
        kwargs=[
            {"key": "company.id", "attr_name": "test_company", "func": None},
        ],
        query_filter=[
            {"key": "companyIDs", "attr_name": "test_company", "func": IdDictBuilder.id_to_list},
        ],
        is_single=True,
        filter_has_company=False
    )
    test_company_admin_user = UserFromCreate("test_company_admin")


@pytest.fixture(scope="module")
def data(data):
    # time.sleep(10)
    logging.info(data.company.id)
    d = MyData(data)
    company_ = d.test_company
    company_.change_permissions(["平台"])
    # time.sleep(10)
    yield d


@allure.feature("企业管理")
@allure.story("创建企业")
class TestCreateCompany(CreateCasesTemplate):
    operator = "new_company"  # 要更新的对象
    assert_jmespath = [
        "address",
        "city",
        "contact",
        "county",
        "email",
        "name",
        "phone",
        "province",
        "uscc"
    ]  # 校验jmespath

    @allure.title("测试公司返回的type id一致")
    def test2(self, data):
        operator = getattr(data, self.operator)
        from jmespath import search
        type_id = search("input.type.id", operator.variables)
        assert CompanyQueryOperator(data.admin).query.query_full().c(
            f"data[?type.id == '{type_id}'].companies[] | [?id == '{operator.id}']"
        )


@allure.feature("企业管理")
@allure.story("更新企业")
class TestUpdateCompany(UpdateCasesTemplate):
    create_factory: Type[BaseFactory] = CompanyFactory  # 创建工厂
    operator = "test_company"  # 要更新的对象
    update_args: List = [
        {"key": "companyType.id", "value": 7}
    ]  # 更新的参数
    assert_jmespath: List[str or List[str]] = [
        "address",
        "city",
        "contact",
        "county",
        "email",
        "name",
        "phone",
        "province",
        "uscc"
    ]  # 校验jmespath
    users: List[str] = ["test_company_admin_user"]

    def other_assert(self, operator, update, data):
        from jmespath import search
        type_id = search("input.companyType.id", update.variables)
        assert CompanyQueryOperator(data.admin).query.query_full().c(
            f"data[?type.id == '{type_id}'].companies[] | [?id == '{operator.id}']"
        )


@allure.feature("企业管理")
@allure.story("删除企业")
class TestDeleteCompany(DeleteCasesTemplate):
    operator = "test_company"  # 要删除的对象


@allure.feature("企业管理")
@allure.story("查询企业")
class TestQueryCompanies(QueryFilterCasesTemplate):
    query = CompanyQueryOperator
    user = "admin"

    filters_info = [
        {
            "filter_key": "search",
            "data": [
                {"filter_value": lambda x: x.company1.info["name"][:-1], "value": ["company1"]},
                {"filter_value": lambda x: x.company2.info["name"][:-1], "value": ["company2"]},
            ]
        }
    ]
