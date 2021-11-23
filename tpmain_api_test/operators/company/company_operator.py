from graphql_api_object import BaseOperator

from ...apis.Query_apis import CompanyApps, MyAppList, RoleList
from ...apis.Mutation_apis import DeleteCompanies, SetCompanyAdminPermission, AddCompanyApps, UpdateCompany
from ...schema.platform_schema import CompanyAdminPermissionInput
from ...utils import return_id_dict, return_id_input


class CompanyOperator(BaseOperator):
    update_api = UpdateCompany
    delete_api = DeleteCompanies

    def delete(self):
        return self.delete_api(self.user).run(input={"ids": [self.id]})

    @property
    def apps(self):
        return CompanyApps(self.user).set_filter(companyID=self.id).query().c("data[].name")

    def add_apps(self, app_names: list):
        app_list = MyAppList(self.user).set_filter(company=return_id_dict(self.id)).query(limit=100)
        app_ids = [app_list.search_result("name", i)["id"] for i in app_names]
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

    @property
    def permissions(self):
        return RoleList(self.user).query_full(
            filter={"scope": ["COMPANY_ADMIN"], "company": {"id": self.id}}
        ).c("data[0].permissions[].name")

    def update_type(self, type_id):
        return self.update_part({"companyType": {"id": type_id}})

    def update_name(self, name):
        return self.update_part({"name": name})

    def update_uscc(self, uscc):
        return self.update_part({"uscc": uscc}).c("uscc")
