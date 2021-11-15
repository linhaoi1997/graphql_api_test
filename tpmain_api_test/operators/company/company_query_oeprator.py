from graphqlapiobject import BaseQueryOperator

from .my_api import MyTypeCompanies


class CompanyQueryOperator(BaseQueryOperator):
    query_api = MyTypeCompanies
    filter_has_company: bool = False

    @property
    def ids(self):
        return self.query.c("data[].companies[] | [].id")
