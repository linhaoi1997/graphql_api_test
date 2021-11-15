from .tools import *
from .common_object import *
from graphqlapiobject import BaseUser, GraphqlApi
from ..schema.platform_schema import Mutation, Query
import os


class Me(GraphqlApi):
    api = Query.me


class User(BaseUser):
    url = os.environ.get("URL")

    def __init__(self, account, password):
        proxy_ = os.environ.get("PROXY")
        if proxy_:
            proxy = {
                "http": 'http://' + proxy_,
                "https": 'http://' + proxy_
            }
        else:
            proxy = None

        super(User, self).__init__(self.url, Mutation, {"account": account, "password": password}, proxy=proxy)
        me = Me(self).run()
        self.info = me.result
        self.company_id = me.data.get("company", {}).get("id")
