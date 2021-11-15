from ...apis import TypeCompanies


class MyTypeCompanies(TypeCompanies):

    @property
    def ids(self):
        return self.c("data[].companies[].id")

    def query(self, **kwargs):
        self.set("__fields__")
        return self.__query(**kwargs)

    def query_full(self, **kwargs):
        return self.query(**kwargs)

    def query_ids(self, **kwargs):
        return self.query(**kwargs)

    def __query(self, **kwargs):
        if not kwargs.get("filter") and self.filter:
            kwargs["filter"] = self.filter
        self.filter = {}
        return self.run(scenario="COMPANY", **kwargs)
