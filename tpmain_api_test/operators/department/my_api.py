import json

from tpmain_api_test import TreeObject
from tpmain_api_test.apis import DepartmentTree


class DepartmentTreeObject(TreeObject):
    parent_field = "parent_id"
    child_field = "children"


class MyDepartmentTree(DepartmentTree):

    @property
    def tree(self):
        return DepartmentTreeObject(**json.loads(self.result))

    def search(self, path):
        tree = self.tree
        names = path.split(".")
        node = tree
        for name in names:
            node = node.select_deep("name", name)
        return node

    def search_from_id(self, id_):
        tree = self.tree
        node = tree.select_deep("id", id_)
        return node
