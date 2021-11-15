from graphqlapiobject import BaseOperator

from .my_api import MyDepartmentTree
from ...apis.Mutation_apis import DeleteDepartment, UpdateDepartment


class DepartmentOperator(BaseOperator):
    query_list_api = MyDepartmentTree
    update_api = UpdateDepartment

    def detail(self):
        self._query_list.run(filter=self.query_filter)
        return self._query_list.search_from_id(self.id)

    def delete(self):
        return DeleteDepartment(self.user).run(id=self.id)
