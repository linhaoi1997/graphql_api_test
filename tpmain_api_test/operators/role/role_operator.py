from graphqlapiobject import BaseOperator
from ...apis.Query_apis import RoleList
from ...apis.Mutation_apis import DeleteRole, UpdateRole


class RoleOperator(BaseOperator):
    query_list_api = RoleList

    update_api = UpdateRole
    delete_api = DeleteRole

    def delete(self):
        return self.delete_api(self.user).run(
            id=[self.id]
        )
