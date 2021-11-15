from graphqlapiobject.BaseOperator import BaseFactory
from .user_operator import UserOperator
from ...apis.Mutation_apis import CreateUser
from ...apis.Query_apis import Users


class UserFactory(BaseFactory):
    # 创建部分
    create_api = CreateUser  # 创建调用的接口
    create_args = ["company.id", "department.id", "role"]  # 创建默认的参数,基本参数如company id
    # 查询部分
    query_api = Users  # 查询的列表接口

    query_path = "data"  # 返回结果中对应的列表路径
    query_field = "name"  # 路径下对应的查找的值
    query_value_path = "name"  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator = UserOperator
