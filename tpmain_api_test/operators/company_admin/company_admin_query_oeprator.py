from graphql_api_object import BaseQueryOperator
from ...apis.Query_apis import CompanyAdminUsers


class CompanyAdminQueryOperator(BaseQueryOperator):
    query_api = CompanyAdminUsers
