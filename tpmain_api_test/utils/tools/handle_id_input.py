from collections import Iterable

from tpmain_api_test.schema.platform_schema import IDInput


def return_id_input(ids):
    if isinstance(ids, Iterable) and not isinstance(ids, str):
        return [IDInput(id=i) for i in ids]
    else:
        return IDInput(id=ids)


def return_id_dict(ids):
    if isinstance(ids, Iterable) and not isinstance(ids, str):
        return [[{"id": i} for i in ids]]
    else:
        return {"id": ids}
