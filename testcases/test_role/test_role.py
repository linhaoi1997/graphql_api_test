import logging

import allure
from graphql_api_object import fake

from tpmain_api_test.define_permissions import PlatformMenuPermission, DataPermission


@allure.feature("角色管理")
@allure.story("角色业务")
class TestCreateRole:

    @allure.title("更新角色权限")
    def test1(self, new_role):
        new_role.update_permissions({PlatformMenuPermission.my_apps: DataPermission.OWN})
        permissions = new_role.permissions
        logging.info(permissions)
        for i in permissions:
            if i["name"] == PlatformMenuPermission.my_apps:
                assert i["range"] == DataPermission.OWN
                break
        else:
            raise AssertionError("没找到对应权限")

    @allure.title("更新角色名称")
    def test2(self, new_role):
        new_name = fake.name
        new_role.update_name(new_name)
        assert new_role["name"] == new_name
