class PlatformAppMenuPermission:
    auto_form = "示例表单"
    bi = "BI"


class PlatformMenuPermission:
    platform = "平台"
    manage = "管理中心"
    company_manage = "企业管理"
    company_account_manage = "用户管理"
    company_role_manage = "角色管理"
    company_organization_manage = "组织管理"
    my_apps = "我的应用"
    workbench = "平台工作台"


class CompanyPermissions:
    view_company = "查询企业"
    add_company = "添加企业"
    delete_company = "删除企业"

    view_company_permission = "查询企管员菜单权限"
    edit_company_permission = "编辑企管员菜单权限"

    view_company_admin = "查询企管员账号"
    create_company_admin = "添加企管员账号"
    edit_company_admin = "编辑企管员账号"
    delete_company_admin = "删除企管员账号"
    reset_admin_password = "重置企管员账号密码"

    add_company_app = "添加企业应用"
    view_company_app = "查询企业应用"
    delete_company_app = "删除企业应用"
    edit_company = "编辑企业信息"


class OrganizationPermissions:
    select_company = "组织管理/选择企业"
    view_company_info = "查询企业信息"
    edit_company_info = "编辑企业信息"
    create_organization = "添加组织"
    view_organization = "查询组织"
    edit_organization = "编辑组织"
    drag_organization = "组织拖拽"
    delete_organization = "删除部门"


class RolePermissions:
    select_company = "角色管理/选择企业"
    create_role = "添加角色"
    view_role = "查询角色"
    edit_role = "编辑角色"
    delete_role = "删除角色"


class AccountPermissions:
    select_company = "角色管理/选择企业"
    create_account = "添加用户"
    view_account = "查询用户"
    edit_account = "编辑用户"
    delete_account = "删除用户"
    reset_account_password = "重置密码"


class ErpCustomerPermissions:
    root = "客户管理"
    customer = "客户清单"
    manager = "客户经理清单"


class ErpSalePermissions:
    root = "销售管理"
    customer = "业务订单"
    manager = "基础配置"


class ErpProductionPermissions:
    root = "生产管理"
    production_notification = "生产通知"
    production_task = "生产单"
    production_plan = "主生产计划"
    erp_department = "生产部门绑定"


class DataPermission:
    ALL = "ALL"
    OWN = "OWN"
