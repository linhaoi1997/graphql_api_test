from graphql_api_object import BaseOperator

from ... import User
from ...apis.Mutation_apis import DeleteUsers, UpdateUser, ResetPassword, UpdateMyPassword


class UserOperator(BaseOperator):
    update_api = UpdateUser
    delete_api = DeleteUsers

    def delete(self):
        return self.delete_api(self.user).run(
            input={
                "ids": [self.id]
            }
        )

    def reset_password(self):
        return ResetPassword(self.user).run(
            input={"userIDs": [self.id]},
            scenario="NORMAL_USER"
        ).c("[0].password")

    @property
    def _role_input(self):
        return [{"id": i["id"] for i in self.info["role"]}]

    def update_part(self, kwargs):
        kwargs["id"] = self.id
        if not kwargs.get("role"):
            kwargs["role"] = self._role_input
        return self.update_api(self.user).run(
            **{"input": kwargs}
        )

    @property
    def client(self):
        return User(self.info["account"], self.info["password"])

    def update_name(self, name):
        return self.update_part({"name": name})

    def update_department(self, department):
        return self.update_part({"department": {"id": department.id}})

    def update_role(self, role: list):
        return self.update_part({"role": [{"id": r.id} for r in role]})

    def active(self):
        return self.update_part({"isActive": True})

    def forbidden(self):
        return self.update_part({"isActive": False})


class EasyPasswordUserOperator(UserOperator):
    def __init__(self, *args):
        super(UserOperator, self).__init__(*args)
        UpdateMyPassword(self.client).run(
            input={
                "oldPassword": self.info["password"],
                "newPassword": "123456",
            }
        )
        self.info["password"] = "123456"
