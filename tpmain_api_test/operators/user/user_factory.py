from graphql_api_object import BaseFactory, IdDictBuilder
from .user_operator import UserOperator, EasyPasswordUserOperator
from ...apis.Mutation_apis import CreateUser
from ...apis.Query_apis import Users


class UserFactory(BaseFactory):
    # 创建部分
    create_api = CreateUser  # 创建调用的接口
    create_args = [
        {"attr": "company", "key": "company.id", "func": None},
        {"attr": "department", "key": "department.id", "func": None},
        {"attr": "role", "key": "role", "func": IdDictBuilder.id_to_dict_list}
    ]  # 创建默认的参数,基本参数如company id
    # 查询部分
    query_api = Users  # 查询的列表接口
    query_args = []

    query_path = "data"  # 返回结果中对应的列表路径
    query_field = "name"  # 路径下对应的查找的值
    query_value_path = "name"  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator = UserOperator

    @classmethod
    def _query_single(cls, query_api, query_value, create_api):
        info = super(UserFactory, cls)._query_single(query_api, query_value, create_api)
        info["password"] = create_api.result
        return info


class EasyPasswordUserFactory(UserFactory):
    operator = EasyPasswordUserOperator
