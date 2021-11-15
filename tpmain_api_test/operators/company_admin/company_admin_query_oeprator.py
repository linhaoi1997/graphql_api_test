from graphqlapiobject import BaseQueryOperator
from ...apis.Query_apis import CompanyAdminUsers


class CompanyAdminQueryOperator(BaseQueryOperator):
    query_api = CompanyAdminUsers
