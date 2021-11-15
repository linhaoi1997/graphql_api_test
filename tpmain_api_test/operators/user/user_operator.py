from graphqlapiobject import BaseOperator
from ...apis.Query_apis import Users, User
from ...apis.Mutation_apis import DeleteUsers, UpdateUser


class UserOperator(BaseOperator):
    query_list_api = Users

    update_api = UpdateUser
    delete_api = DeleteUsers

    def delete(self):
        return self.delete_api(self.user).run(
            input={
                "ids": [self.id]
            }
        )
