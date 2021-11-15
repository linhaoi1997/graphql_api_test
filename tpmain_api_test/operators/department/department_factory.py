from typing import List, Dict

from .my_api import MyDepartmentTree
from ...apis.Mutation_apis import CreateDepartment
from .department_operator import DepartmentOperator
from graphqlapiobject import BaseFactory, GraphqlOperationAPi


class DepartmentFactory(BaseFactory):
    # 创建部分
    create_api = CreateDepartment  # 创建调用的接口
    create_args: Dict = ["parent.id"]  # 创建默认的参数,基本参数如company id
    # 查询部分
    query_api = MyDepartmentTree  # 查询的列表接口
    query_args = ["company"]
    # 返回操作器部分
    operator = DepartmentOperator

    @classmethod
    def _query_from_list(cls, user, create_api: GraphqlOperationAPi, query_filter) -> List[Dict] or Dict:
        q = cls.query_api(user).run(filter=query_filter)
        name = create_api.search_from_input("input.name")
        return q.search(name)


class RootDepartment:

    def __init__(self, user_name):
        self.user_name = user_name

    def __get__(self, instance, owner):
        user = getattr(instance, self.user_name)
        company = instance.company.id
        query_filter = {"company": {"id": company}}
        root = MyDepartmentTree(user).run(
            filter=query_filter
        ).tree
        return DepartmentOperator(user, root, {}, query_filter)
