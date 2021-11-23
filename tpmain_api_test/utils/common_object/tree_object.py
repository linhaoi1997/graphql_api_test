class TreeType(type):
    """树的数据结构，使用此元类的所有类，会根据parent_field和child_field生成一棵树"""

    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args)
        for name, value in kwargs.items():
            if name == obj.parent_field:
                setattr(obj, "parent", value)
            elif name == obj.child_field:
                setattr(obj, "children", [])
                for child in value:
                    obj.children.append(TreeType.__call__(cls, *args, **child))
            else:
                setattr(obj, name, value)
        return obj


class TreeObject(object, metaclass=TreeType):
    parent_field = "parent_id"
    child_field = "children"

    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return "type" + str(self.__dict__)

    def select(self, field_name, name):
        """如果本节点或者一层子节点的field_name中名称有和name一样的，那么返回这个节点"""
        if getattr(self, field_name) == name:
            return self
        else:
            for child in getattr(self, "children", []):
                if getattr(child, field_name) == name:
                    return child
            else:
                raise AssertionError("no value %s in field %s" % (name, field_name))

    def select_deep(self, field_name, name):
        """如果接口返回的field_name中名称有和name一样的，那么返回这个节点，如果没有查找子节点"""
        if getattr(self, field_name) == name:
            return self
        else:
            for child in getattr(self, "children", []):
                try:
                    result = child.select_deep(field_name, name)
                    if result:
                        return result
                except AssertionError:
                    pass
        raise AssertionError("no value %s in field %s" % (name, field_name))

    def select_path(self, field_name, name, path=None):
        """如果接口返回的field_name中名称有和name一样的，那么返回从根节点到这个节点的所有路径节点"""
        if path is None:
            path = []
        if getattr(self, field_name) == name:
            return True
        else:
            for child in getattr(self, "children", []):
                try:
                    if child.select_path(field_name, name, path):
                        path.insert(0, child)
                        return path
                except AssertionError:
                    pass
        raise AssertionError("no value %s in field %s" % (name, field_name))

    def __iter__(self):
        """遍历树的每个节点"""
        yield self
        for i in getattr(self, "children", []):
            yield from i

    @property
    def sub_fields(self):
        """封装所有子节点成一个列表"""
        return list(iter(self))

    def __getitem__(self, item):
        return getattr(self, item)

    def get(self, name):
        return getattr(self, name)


class TreeObjectList(object):
    """对于有多个根节点的树使用这个object"""
    tree_object = None

    def __init__(self, data: list):
        self.tree_list = []
        for i in data:
            self.tree_list.append(self.tree_object(**i))

    def select(self, field_name, name):
        for tree in self.tree_list:
            try:
                result = tree.select(field_name, name)
                if result:
                    return result
            except AssertionError:
                pass
        raise AssertionError("no value %s in field %s" % (name, field_name))

    def select_deep(self, field_name, name):
        """如果接口返回的field_name中名称有和name一样的，那么返回这个节点，如果没有查找子节点"""
        for tree in self.tree_list:
            try:
                result = tree.select_deep(field_name, name)
                if result:
                    return result
            except AssertionError:
                pass
        return False
        # raise AssertionError("no value %s in field %s" % (name, field_name))

    def select_path(self, field_name, name):
        """如果接口返回的field_name中名称有和name一样的，那么返回从根节点到这个节点的所有路径节点"""
        for tree in self.tree_list:
            try:
                path = tree.select_path(field_name, name)
                if path:
                    if not isinstance(path, list):
                        path = []
                    path.insert(0, tree)
                    return path
            except AssertionError:
                pass
        return False
        # raise AssertionError("no value %s in field %s" % (name, field_name))
