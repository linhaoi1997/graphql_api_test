from graphql_api_object import GraphqlApi, GraphqlOperationAPi, GraphqlUpdateApi, GraphqlQueryListAPi, GraphqlQueryAPi
from ..schema.platform_schema import Mutation


class CreateCompany(GraphqlOperationAPi):
    api = Mutation.create_company


class UpdateCompany(GraphqlUpdateApi):
    api = Mutation.update_company


class DeleteCompanies(GraphqlUpdateApi):
    api = Mutation.delete_companies


class UpdateMyCompany(GraphqlUpdateApi):
    api = Mutation.update_my_company


class CreateDepartment(GraphqlOperationAPi):
    api = Mutation.create_department


class UpdateDepartment(GraphqlUpdateApi):
    api = Mutation.update_department


class DeleteDepartment(GraphqlUpdateApi):
    api = Mutation.delete_department


class CreateCompanyBIDatasource(GraphqlOperationAPi):
    api = Mutation.create_company_bidatasource


class DeleteCompanyBIDatasource(GraphqlUpdateApi):
    api = Mutation.delete_company_bidatasource


class UpdateNotificationConfig(GraphqlUpdateApi):
    api = Mutation.update_notification_config


class ReadNotification(GraphqlQueryAPi):
    api = Mutation.read_notification


class ReadAllNotification(GraphqlQueryAPi):
    api = Mutation.read_all_notification


class CreateFile(GraphqlOperationAPi):
    api = Mutation.create_file


class CreateFiles(GraphqlOperationAPi):
    api = Mutation.create_files


class CreateImage(GraphqlOperationAPi):
    api = Mutation.create_image


class CreateImages(GraphqlOperationAPi):
    api = Mutation.create_images


class CreateMarketFile(GraphqlOperationAPi):
    api = Mutation.create_market_file


class CreateMarketFiles(GraphqlOperationAPi):
    api = Mutation.create_market_files


class CreateRole(GraphqlOperationAPi):
    api = Mutation.create_role


class UpdateRole(GraphqlUpdateApi):
    api = Mutation.update_role


class DeleteRole(GraphqlUpdateApi):
    api = Mutation.delete_role


class SetCompanyAdminPermission(GraphqlUpdateApi):
    api = Mutation.set_company_admin_permission


class CreateSystemIssue(GraphqlOperationAPi):
    api = Mutation.create_system_issue


class UpdateSystemIssue(GraphqlUpdateApi):
    api = Mutation.update_system_issue


class CreateEducationIssue(GraphqlOperationAPi):
    api = Mutation.create_education_issue


class UpdateEducationIssue(GraphqlUpdateApi):
    api = Mutation.update_education_issue


class CreateHelpIssue(GraphqlOperationAPi):
    api = Mutation.create_help_issue


class UpdateHelpIssue(GraphqlUpdateApi):
    api = Mutation.update_help_issue


class RegisterUser(GraphqlQueryAPi):
    api = Mutation.register_user


class Login(GraphqlQueryAPi):
    api = Mutation.login


class Logout(GraphqlQueryAPi):
    api = Mutation.logout


class CreateCompanyAdminUser(GraphqlOperationAPi):
    api = Mutation.create_company_admin_user


class UpdateCompanyAdminUser(GraphqlUpdateApi):
    api = Mutation.update_company_admin_user


class DeleteCompanyAdminUsers(GraphqlUpdateApi):
    api = Mutation.delete_company_admin_users


class CreateUser(GraphqlOperationAPi):
    api = Mutation.create_user


class UpdateUser(GraphqlUpdateApi):
    api = Mutation.update_user


class ImportUser(GraphqlQueryAPi):
    api = Mutation.import_user


class DeleteUsers(GraphqlUpdateApi):
    api = Mutation.delete_users


class UpdateMe(GraphqlUpdateApi):
    api = Mutation.update_me


class UpdateMyPassword(GraphqlUpdateApi):
    api = Mutation.update_my_password


class ResetPassword(GraphqlQueryAPi):
    api = Mutation.reset_password


class RestoreUser(GraphqlQueryAPi):
    api = Mutation.restore_user


class ActivateUser(GraphqlQueryAPi):
    api = Mutation.activate_user


class ForbiddenUser(GraphqlQueryAPi):
    api = Mutation.forbidden_user


class OauthAuthorize(GraphqlQueryAPi):
    api = Mutation.oauth_authorize


class CreateMarketSolution(GraphqlOperationAPi):
    api = Mutation.create_market_solution


class UpdateMarketSolution(GraphqlUpdateApi):
    api = Mutation.update_market_solution


class PublishMarketSolution(GraphqlQueryAPi):
    api = Mutation.publish_market_solution


class DeleteMarketSolution(GraphqlUpdateApi):
    api = Mutation.delete_market_solution


class AddCompanyApps(GraphqlOperationAPi):
    api = Mutation.add_company_apps


class DeleteCompanyApps(GraphqlUpdateApi):
    api = Mutation.delete_company_apps


class VisitApp(GraphqlQueryAPi):
    api = Mutation.visit_app


class SetQuickAccessApp(GraphqlUpdateApi):
    api = Mutation.set_quick_access_app


class CreateApp(GraphqlOperationAPi):
    api = Mutation.create_app


class UpdateApp(GraphqlUpdateApi):
    api = Mutation.update_app


class SetThirdPartyAppPermission(GraphqlUpdateApi):
    api = Mutation.set_third_party_app_permission


class DeleteApp(GraphqlUpdateApi):
    api = Mutation.delete_app


class SetWorkbench(GraphqlUpdateApi):
    api = Mutation.set_workbench


class CreateMarketApp(GraphqlOperationAPi):
    api = Mutation.create_market_app


class UpdateMarketApp(GraphqlUpdateApi):
    api = Mutation.update_market_app


class PublishMarketApp(GraphqlQueryAPi):
    api = Mutation.publish_market_app


class DeleteMarketApp(GraphqlUpdateApi):
    api = Mutation.delete_market_app


class CreateMarketIssue(GraphqlOperationAPi):
    api = Mutation.create_market_issue


class UpdateMarketIssue(GraphqlUpdateApi):
    api = Mutation.update_market_issue


