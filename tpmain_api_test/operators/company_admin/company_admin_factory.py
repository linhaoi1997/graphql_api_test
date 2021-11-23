from graphql_api_object import BaseFactory, IdDictBuilder
from .company_admin_operator import CompanyAdminOperator, EasyPasswordCompanyAdminOperator
from ...apis.Mutation_apis import CreateCompanyAdminUser
from ...apis.Query_apis import CompanyAdminUsers


class CompanyAdminFactory(BaseFactory):
    # 创建部分
    create_api = CreateCompanyAdminUser  # 创建调用的接口
    # 查询部分
    query_api = CompanyAdminUsers  # 查询的列表接口
    query_args = [
        {"attr": "company", "key": "companyIDs", "func": IdDictBuilder.id_to_list},
    ]

    query_path = "data"  # 返回结果中对应的列表路径
    query_field = "account"  # 路径下对应的查找的值
    query_value_path = "account"  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator = CompanyAdminOperator

    @classmethod
    def send_query_request(cls, user, query_filter):
        if query_filter is None:
            query_filter = {}
        final_filter = cls.prepare_query_args(user, query_filter)
        return cls.query_api(user).set_filter(**final_filter).query_full(limit=100), final_filter

    @classmethod
    def _query_single(cls, query_api, query_value, create_api):
        info = super(CompanyAdminFactory, cls)._query_single(query_api, query_value, create_api)
        info["password"] = create_api.result
        return info


class EasyPasswordCompanyAdminFactory(CompanyAdminFactory):
    operator = EasyPasswordCompanyAdminOperator
