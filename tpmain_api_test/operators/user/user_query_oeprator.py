from graphql_api_object import BaseQueryOperator
from ...apis.Query_apis import Users


class UsersQueryOperator(BaseQueryOperator):
    query_api = Users
