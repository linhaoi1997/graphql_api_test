import json

from graphqlapiobject.BaseOperator import BaseFactory
from .role_operator import RoleOperator
from ...apis.Mutation_apis import CreateRole
from ...apis.Query_apis import RoleList, PermissionTree
from ...define_permissions import DataPermission, PlatformMenuPermission
from ...schema.platform_schema import PermissionTreeFilterInput, IDInput
from ...utils import TreeObject, TreeObjectList


class PermissionObject(TreeObject):
    child_field = "child"
    parent_field = "parent_id"


class PermissionsTreeObject(TreeObjectList):
    tree_object = PermissionObject


class MyPermissionTree(PermissionTree):

    def __init__(self, user):
        super(PermissionTree, self).__init__(user)
        self.trees = {}

    def query_company_permissions(self, company_id):
        # company_id必传
        assert company_id
        self.run(filter=PermissionTreeFilterInput(company=IDInput(id=company_id), scope="company"))
        return PermissionsTreeObject(json.loads(self.result))

    def search_permission(self, name, company_id=None):
        if not self.trees.get(str(company_id)):
            self.trees[str(company_id)] = self.query_company_permissions(company_id)
        tree = self.trees[str(company_id)]
        if "/" not in name:
            nodes = tree.select_path("name", name)
            return nodes
        else:
            names = name.split("/")
            nodes = tree.select_path("name", names[0])
            for i in names[1:]:
                node = nodes[-1].select_path("name", i)
                nodes.append(node[0])
            return nodes

    def search_permission_path(self, name, company_id=None):
        """选中某个权限，返回该节点所有子节点的权限和从根节点到这个节点的所有路线的权限"""
        nodes = self.search_permission(name, company_id)
        nodes.extend(nodes[-1].sub_fields[1:])
        return [i.id for i in nodes]

    def search_permission_nodes(self, name, company_id=None):
        """选中某个权限，返回该节点所有子节点的权限和从根节点到这个节点的所有路线的权限"""
        nodes = self.search_permission(name, company_id)
        nodes.extend(nodes[-1].sub_fields[1:])
        return nodes


class RoleFactory(BaseFactory):
    # 创建部分
    create_api = CreateRole  # 创建调用的接口
    create_args = ["permissions"]  # 创建默认的参数,基本参数如company id
    # 查询部分
    query_api = RoleList  # 查询的列表接口

    query_path = "data"  # 返回结果中对应的列表路径
    query_field = "name"  # 路径下对应的查找的值
    query_value_path = "name"  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator = RoleOperator

    base_permission_info = {
        PlatformMenuPermission.my_apps: DataPermission.OWN
    }

    permission_info = {}

    @classmethod
    def make_args(cls, user, kwargs):
        from copy import copy
        company_id = kwargs.get("company.id")
        t = MyPermissionTree(user)
        permissions = []
        permissions_info = copy(cls.base_permission_info)
        permissions_info.update(cls.permission_info)
        for permission in permissions_info.keys():
            r = t.search_permission_nodes(permission, company_id)
            for i in r:
                if i.id not in [j.id for j in permissions]:
                    permissions.append(i)
        permissions_input = cls.return_permission_input(permissions, permissions_info)
        return {"permissions": permissions_input}

    @classmethod
    def return_permission_input(cls, permissions, permissions_info):
        """赋予permission数据权限"""
        result = []
        for permission in permissions:
            for permission_name in permissions_info.keys():
                if permission_name.endswith(permission.name):
                    data_range = permissions_info[permission_name]
                    break
            else:
                data_range = "ALL"
            result.append({"dataRange": data_range, "permission": {"id": permission.id}})
        return result
