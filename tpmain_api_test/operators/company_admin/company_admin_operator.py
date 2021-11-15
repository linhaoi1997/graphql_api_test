from graphqlapiobject import BaseOperator

from ...apis.Query_apis import CompanyAdminUsers
from ...apis.Mutation_apis import DeleteCompanyAdminUsers, ResetPassword, UpdateCompanyAdminUser
from ...utils import User


class CompanyAdminOperator(BaseOperator):
    query_list_api = CompanyAdminUsers
    query_path: str = "data"

    update_api = UpdateCompanyAdminUser
    delete_api = DeleteCompanyAdminUsers

    def delete(self):
        return DeleteCompanyAdminUsers(self.user).run(input={"ids": [self.id]})

    def reset_password(self):
        return ResetPassword(self.user).run(
            input={"userIDs": [self.id]},
            scenario="COMPANY_ADMIN"
        )

    @property
    def client(self):
        return User(self.info["account"], self.info["password"])
