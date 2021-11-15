from graphqlapiobject import BaseQueryOperator
from ...apis.Query_apis import Users


class UsersQueryOperator(BaseQueryOperator):
    query_api = Users
