from graphql_api_object.base_operator.base_test_cases_template import *

import allure

from tpmain_api_test import User
from tpmain_api_test.apis import CompanyAdminUsers
from tpmain_api_test.operators import CompanyAdminOperator


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
@allure.story("删除企业管理员")
class TestDeleteCompanyAdminUser(DeleteCasesTemplate):
    operator = "new_company_admin"  # 要删除的对象


@allure.feature("企业管理")
@allure.story("分页企业管理员")
class TestQueryCompanyAdminUsers(QueryPagingCasesTemplate):
    query_api = CompanyAdminUsers
    user = "admin"
    resource: str = "new_company_admin"  # base_data中的属性

    def make_query_args(self, data):
        return {"filter": {"companyIDs": [getattr(data, "company").id]}}
