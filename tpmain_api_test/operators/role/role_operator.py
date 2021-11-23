from graphql_api_object import BaseOperator
from ...apis.Mutation_apis import DeleteRole, UpdateRole
from ...define_permissions import PlatformMenuPermission, DataPermission


class RoleOperator(BaseOperator):
    update_api = UpdateRole
    delete_api = DeleteRole

    def delete(self):
        return self.delete_api(self.user).run(
            id=[self.id]
        )

    def update_permissions(self, permission_info):
        from tpmain_api_test.operators.role.role_factory import return_permissions_input
        permissions_input = return_permissions_input(self.user, permission_info, self.user.info["company"]["id"])
        return self.update_part(
            permissions_input
        )

    def update_name(self, name):
        from tpmain_api_test.operators.role.role_factory import return_permissions_input
        permission_info = {PlatformMenuPermission.my_apps: DataPermission.OWN}
        permissions_input = return_permissions_input(self.user, permission_info, self.user.info["company"]["id"])
        permissions_input["name"] = name
        return self.update_part(
            permissions_input
        )

    @property
    def permissions(self):
        return self["permissions"]
