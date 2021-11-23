import logging

from graphql_api_object import BaseOperator

from ...apis.Mutation_apis import DeleteDepartment, UpdateDepartment
from ...apis.Query_apis import DepartmentNameSameAsSiblings


class DepartmentOperator(BaseOperator):
    update_api = UpdateDepartment

    def detail(self):
        self._query_list.run(filter=self.query_filter)
        return self._query_list.search_from_id(self.id)

    def delete(self):
        return DeleteDepartment(self.user).run(id=self.id)

    def name_exists(self, name: str):
        logging.info(self.info)
        return DepartmentNameSameAsSiblings(self.user).run(
            filter={"name": name, "parent": {"id": self.info["parent"]}}
        ).result

    def name_exists_with_id(self, name):
        return DepartmentNameSameAsSiblings(self.user).run(
            filter={"name": name, "parent": {"id": self.info["parent"]}, "id": self.id}
        ).result
