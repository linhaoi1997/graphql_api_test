from graphql_api_object.base_operator.base_test_cases_template import *

from tpmain_api_test.operators import CompanyQueryOperator


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
@allure.story("删除企业")
class TestDeleteCompany(DeleteCasesTemplate):
    operator = "new_company"  # 要删除的对象


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
