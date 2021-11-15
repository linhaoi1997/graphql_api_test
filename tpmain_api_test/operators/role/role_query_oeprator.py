from graphqlapiobject import BaseQueryOperator
from ...apis.Query_apis import RoleList


class RoleQueryOperator(BaseQueryOperator):
    query_api = RoleList
