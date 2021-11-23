from graphql_api_object import BaseQueryOperator
from ...apis.Query_apis import RoleList


class RoleQueryOperator(BaseQueryOperator):
    query_api = RoleList
