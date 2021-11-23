from graphql_api_object import BaseOperator

from ...apis import Me
from ...apis.Mutation_apis import DeleteCompanyAdminUsers, ResetPassword, UpdateCompanyAdminUser, UpdateMyPassword
from ...utils import User


class CompanyAdminOperator(BaseOperator):
    update_api = UpdateCompanyAdminUser
    delete_api = DeleteCompanyAdminUsers

    def delete(self):
        return DeleteCompanyAdminUsers(self.user).run(input={"ids": [self.id]})

    def reset_password(self):
        return ResetPassword(self.user).run(
            input={"userIDs": [self.id]},
            scenario="COMPANY_ADMIN"
        ).c("[0].password")

    @property
    def permissions(self):
        return Me(self.client).set("role.permissions.name").run().c(".role[0].permissions[].name")

    @property
    def client(self):
        return User(self.info["account"], self.info["password"])

    def update_name(self, name):
        return self.update_part({"name": name})


class EasyPasswordCompanyAdminOperator(CompanyAdminOperator):
    def __init__(self, *args):
        super(EasyPasswordCompanyAdminOperator, self).__init__(*args)
        UpdateMyPassword(self.client).run(
            input={
                "oldPassword": self.info["password"],
                "newPassword": "123456",
            }
        )
        self.info["password"] = "123456"
