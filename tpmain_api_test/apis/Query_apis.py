from graphqlapiobject import GraphqlApi, GraphqlOperationAPi, GraphqlUpdateApi, GraphqlQueryListAPi, GraphqlQueryAPi
from ..schema.platform_schema import Query


class CompanyExists(GraphqlQueryListAPi):
    api = Query.company_exists


class CompanyTypeList(GraphqlQueryListAPi):
    api = Query.company_type_list


class Countries(GraphqlQueryListAPi):
    api = Query.countries


class Provinces(GraphqlQueryListAPi):
    api = Query.provinces


class Cities(GraphqlQueryListAPi):
    api = Query.cities


class Counties(GraphqlQueryListAPi):
    api = Query.counties


class Company(GraphqlQueryAPi):
    api = Query.company


class Companies(GraphqlQueryListAPi):
    api = Query.companies


class CityCompanies(GraphqlQueryListAPi):
    api = Query.city_companies


class TypeCompanies(GraphqlQueryListAPi):
    api = Query.type_companies


class MyCompany(GraphqlQueryAPi):
    api = Query.my_company


class DepartmentTree(GraphqlQueryAPi):
    api = Query.department_tree


class DepartmentList(GraphqlQueryListAPi):
    api = Query.department_list


class DepartmentNameSameAsSiblings(GraphqlQueryListAPi):
    api = Query.department_name_same_as_siblings


class CompanyBIDatasourceList(GraphqlQueryListAPi):
    api = Query.company_bidatasource_list


class CompanyBIDatasourceTree(GraphqlQueryAPi):
    api = Query.company_bidatasource_tree


class NotificationConfigList(GraphqlQueryListAPi):
    api = Query.notification_config_list


class NotificationConfig(GraphqlQueryAPi):
    api = Query.notification_config


class NotificationList(GraphqlQueryListAPi):
    api = Query.notification_list


class Notification(GraphqlQueryAPi):
    api = Query.notification


class NotificationConfigApp(GraphqlQueryAPi):
    api = Query.notification_config_app


class NotificationApp(GraphqlQueryAPi):
    api = Query.notification_app


class UploadConfig(GraphqlQueryAPi):
    api = Query.upload_config


class UploadConfigs(GraphqlQueryListAPi):
    api = Query.upload_configs


class RoleList(GraphqlQueryListAPi):
    api = Query.role_list


class PermissionTree(GraphqlQueryAPi):
    api = Query.permission_tree


class PermissionList(GraphqlQueryListAPi):
    api = Query.permission_list


class RoleExists(GraphqlQueryListAPi):
    api = Query.role_exists


class Issues(GraphqlQueryListAPi):
    api = Query.issues


class ExportIssues(GraphqlQueryListAPi):
    api = Query.export_issues


class Issue(GraphqlQueryAPi):
    api = Query.issue


class AccountExists(GraphqlQueryListAPi):
    api = Query.account_exists


class Me(GraphqlQueryAPi):
    api = Query.me


class CompanyAdminUsers(GraphqlQueryListAPi):
    api = Query.company_admin_users


class PlatformAdminUsers(GraphqlQueryListAPi):
    api = Query.platform_admin_users


class Users(GraphqlQueryListAPi):
    api = Query.users


class PlatformUserList(GraphqlQueryListAPi):
    api = Query.platform_user_list


class User(GraphqlQueryAPi):
    api = Query.user


class UserTemplate(GraphqlQueryAPi):
    api = Query.user_template


class ExportUser(GraphqlQueryAPi):
    api = Query.export_user


class SupportUsers(GraphqlQueryListAPi):
    api = Query.support_users


class AppUsers(GraphqlQueryListAPi):
    api = Query.app_users


class OauthPermissionList(GraphqlQueryListAPi):
    api = Query.oauth_permission_list


class MarketSolutionList(GraphqlQueryListAPi):
    api = Query.market_solution_list


class MarketSolution(GraphqlQueryAPi):
    api = Query.market_solution


class MarketSolutionSummary(GraphqlQueryAPi):
    api = Query.market_solution_summary


class AppList(GraphqlQueryListAPi):
    api = Query.app_list


class App(GraphqlQueryAPi):
    api = Query.app


class CompanyApps(GraphqlQueryListAPi):
    api = Query.company_apps


class MyCompanyApps(GraphqlQueryListAPi):
    api = Query.my_company_apps


class MyAppList(GraphqlQueryListAPi):
    api = Query.my_app_list


class QuickAccessApp(GraphqlQueryAPi):
    api = Query.quick_access_app


class RecentApp(GraphqlQueryAPi):
    api = Query.recent_app


class AppConfig(GraphqlQueryAPi):
    api = Query.app_config


class Workbench(GraphqlQueryAPi):
    api = Query.workbench


class WorkbenchCardOption(GraphqlQueryAPi):
    api = Query.workbench_card_option


class WorkbenchCardData(GraphqlQueryAPi):
    api = Query.workbench_card_data


class SystemLogList(GraphqlQueryListAPi):
    api = Query.system_log_list


class SystemLogAction(GraphqlQueryAPi):
    api = Query.system_log_action


class MarketAppList(GraphqlQueryListAPi):
    api = Query.market_app_list


class MarketApp(GraphqlQueryAPi):
    api = Query.market_app


class MarketAppSummary(GraphqlQueryAPi):
    api = Query.market_app_summary


class MarketIssueList(GraphqlQueryListAPi):
    api = Query.market_issue_list


class MarketIssue(GraphqlQueryAPi):
    api = Query.market_issue


class MarketIssueSummary(GraphqlQueryAPi):
    api = Query.market_issue_summary


class BiIssueIssue(GraphqlQueryAPi):
    api = Query.bi_issue_issue


class _service(GraphqlQueryAPi):
    api = Query._service


class _entities(GraphqlQueryListAPi):
    api = Query._entities


