from graphqlapiobject import BaseOperator

from .my_api import MyTypeCompanies
from ...apis.Query_apis import CompanyApps, MyAppList, TypeCompanies
from ...apis.Mutation_apis import DeleteCompanies, SetCompanyAdminPermission, AddCompanyApps, UpdateCompany
from ...schema.platform_schema import CompanyAdminPermissionInput
from ...utils import return_id_input


class CompanyOperator(BaseOperator):
    query_list_api = MyTypeCompanies
    query_path: str = "data[].companies[]|"

    update_api = UpdateCompany
    delete_api = DeleteCompanies

    def delete(self):
        return self.delete_api(self.user).run(input={"ids": [self.id]})

    @property
    def apps(self):
        return CompanyApps(self.user).set_filter(companyID=self.id).query()

    def add_apps(self, app_names: list):
        app_list = MyAppList(self.user).set_filter(company=return_id_input(self.id)).query()
        app_ids = [app_list.search_result("name", i).id for i in app_names]
        return AddCompanyApps(self.user).auto_run(
            {
                "companyID": self.id,
                "appIDs": app_ids
            }
        )

    def change_permissions(self, permission_names: list):
        from ..role.role_factory import MyPermissionTree
        permission_tree = MyPermissionTree(self.user)
        permissions = set()

        for permission in permission_names:
            r = permission_tree.search_permission_path(permission, self.id)
            permissions = permissions.union(set(r))

        return SetCompanyAdminPermission(self.user).run(
            input=CompanyAdminPermissionInput(company=return_id_input(self.id),
                                              permission=return_id_input(permissions))
        )
