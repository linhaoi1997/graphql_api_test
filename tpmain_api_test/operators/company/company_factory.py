import random
from graphql_api_object import BaseFactory
from .company_operator import CompanyOperator
from .my_api import MyTypeCompanies
from ...apis.Mutation_apis import CreateCompany
from ...apis.Query_apis import Provinces, Counties, Cities, CompanyTypeList


class CompanyFactory(BaseFactory):
    # 创建部分
    create_api = CreateCompany  # 创建调用的接口
    create_args = []  # 创建默认的参数,基本参数如company id
    # 查询部分
    query_api = MyTypeCompanies  # 查询的列表接口
    query_args = []

    default_attr = {}

    query_path = "data[].companies[]|"  # 返回结果中对应的列表路径
    query_field = "name"  # 路径下对应的查找的值
    query_value_path = "name"  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回业务对象
    operator = CompanyOperator

    @classmethod
    def make_args(cls, user, kwargs):
        province = Provinces(user).run().random()
        try:
            city = Cities(user).run(province_id=province.id).random()
            county = Counties(user).run(city_id=city.id).random()
        except IndexError as e:
            city = Cities(user).run(province_id=province.id).random()
            county = Counties(user).run(city_id=city.id).random()
        company_type = random.choice(CompanyTypeList(user).query().c("data"))
        return {"province": province.name, "city": city.name, "county": county.name, "type.id": company_type["id"]}
