import sgqlc.types


platform_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AppKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SELF', 'ENTERPRISE', 'THIRD_PARTY')


Boolean = sgqlc.types.Boolean

class CardType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('IMAGE', 'TEXT', 'CARD', 'TAB')


Float = sgqlc.types.Float

class Granularity(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DAILY', 'MONTHLY', 'ANNUALLY', 'HOURLY', 'WEEKLY', 'MINUTE', 'FIVE_MINUTE')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class IssueAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DEAL', 'REMARK', 'TRANSFER', 'CLOSE', 'REOPEN')


class IssueCategory(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SYSTEM', 'EDUCTION', 'HELP')


class IssueReason(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OTHER', 'ABNORMAL_DATA', 'SLOW_LOADING')


class IssueStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('READY', 'DEALING', 'CLOSE')


class IssueType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OTHER', 'ABNORMAL_DATA', 'SLOW_LOADING')


class JSON(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JSONString(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JumpKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NEW_WINDOW', 'CURRENT_WINDOW')


class MarketAppType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('RESEARCH_DESIGN', 'MANUFACTURING', 'MAINTENANCE_SERVICE', 'SAFETY_PRODUCTION', 'SUPPLY_CHAIN_MANAGEMENT', 'WAREHOUSE_AND_LOGISTICS', 'OPERATION_MANAGEMENT', 'QUALITY_CONTROL', 'ENERGY_SAVING')


class MarketConsultationType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP', 'SOLUTION')


class MarketIssueAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'FOLLOW', 'TRANSFER', 'CLOSE', 'REOPEN')


class MarketIssueStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('READY', 'DEALING', 'CLOSE')


class MarketSolutionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('RESEARCH_DESIGN', 'MANUFACTURING', 'MAINTENANCE_SERVICE', 'SAFETY_PRODUCTION', 'SUPPLY_CHAIN_MANAGEMENT', 'WAREHOUSE_AND_LOGISTICS', 'OPERATION_MANAGEMENT', 'QUALITY_CONTROL', 'ENERGY_SAVING')


class NotificationKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP', 'PLATFORM')


class PermissionDataRange(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ALL', 'OWN')


class PermissionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP_MENU', 'PLATFORM_MENU', 'FUNCTION', 'INTERFACE')


class ResetPasswordScenario(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NORMAL_USER', 'COMPANY_ADMIN', 'PLATFORM_USER')


class RoleScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PLATFORM', 'COMPANY_ADMIN')


String = sgqlc.types.String

class Timestamp(sgqlc.types.Scalar):
    __schema__ = platform_schema


class TypeCompaniesScenario(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'MY_COMPANY', 'ROLE', 'USER', 'SYSTEM_LOG', 'CUSTOMER')


class UpdateCompanyScenario(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'MY_COMPANY')


class UserOrigin(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('REGISTED', 'ADDED')


class UserType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY_ADMIN', 'COMPANY_NORMAL', 'PLATFORM_ADMIN', 'JIN_HUA_SCHOOL', 'CHANJIAO_SYS_ADMIN', 'CHANJIAO_SCHOOL_ADMIN')


class _Any(sgqlc.types.Scalar):
    __schema__ = platform_schema



########################################################################
# Input Objects
########################################################################
class ActivateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class AddCompanyAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'app_ids')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')
    app_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='appIDs')


class AppListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class AppUserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_codes', 'company')
    app_codes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='appCodes')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class AppsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class AppsOmit(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_ids',)
    company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='companyIDs')


class BIFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'granularity', 'aggregation', 'metric', 'series')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    granularity = sgqlc.types.Field(Granularity, graphql_name='granularity')
    aggregation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregation')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    series = sgqlc.types.Field(String, graphql_name='series')


class CompanyAdminPermissionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'permission')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    permission = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('IDInput')), graphql_name='permission')


class CompanyAdminUsersFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'company_ids', 'department_ids')
    search = sgqlc.types.Field(String, graphql_name='search')
    company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='companyIDs')
    department_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='departmentIDs')


class CompanyAppsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id',)
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')


class CompanyBIDatasourceFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids', 'search', 'county', 'company_type')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    search = sgqlc.types.Field(String, graphql_name='search')
    county = sgqlc.types.Field(String, graphql_name='county')
    company_type = sgqlc.types.Field('IDInput', graphql_name='companyType')


class CompanyTypeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class CreateAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'name', 'kind', 'jump_kind', 'order', 'description', 'avatar', 'url', 'whether_new_client', 'redirect_url')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AppKind), graphql_name='kind')
    jump_kind = sgqlc.types.Field(sgqlc.types.non_null(JumpKind), graphql_name='jumpKind')
    order = sgqlc.types.Field(Float, graphql_name='order')
    description = sgqlc.types.Field(String, graphql_name='description')
    avatar = sgqlc.types.Field('IDInput', graphql_name='avatar')
    url = sgqlc.types.Field(String, graphql_name='url')
    whether_new_client = sgqlc.types.Field(Boolean, graphql_name='whetherNewClient')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')


class CreateCompanyAdminUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'name', 'company', 'phone', 'email')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')


class CreateCompanyBIDatasourceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('datasource', 'company')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='datasource')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')


class CreateCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('type', 'name', 'address', 'uscc', 'contact', 'email', 'phone', 'province', 'city', 'county')
    type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    address = sgqlc.types.Field(String, graphql_name='address')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')


class CreateDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'parent')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='parent')


class CreateFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateImageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'content', 'attachments')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='attachments')


class CreateMarketAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'type', 'cover_image', 'is_recommended', 'brief', 'description', 'screenshot')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketAppType), graphql_name='type')
    cover_image = sgqlc.types.Field('IDInput', graphql_name='coverImage')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='screenshot')


class CreateMarketFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateMarketIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'solution', 'type', 'company_name', 'contact', 'phone', 'email', 'content')
    app = sgqlc.types.Field('IDInput', graphql_name='app')
    solution = sgqlc.types.Field('IDInput', graphql_name='solution')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketConsultationType), graphql_name='type')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class CreateMarketSolutionDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'items', 'image', 'content', 'type')
    title = sgqlc.types.Field(String, graphql_name='title')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketCommonComponentInput')), graphql_name='items')
    image = sgqlc.types.Field('IDInput', graphql_name='image')
    content = sgqlc.types.Field(String, graphql_name='content')
    type = sgqlc.types.Field(sgqlc.types.non_null(CardType), graphql_name='type')


class CreateMarketSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'cover_image', 'type', 'is_recommended', 'brief', 'description', 'app', 'detail')
    title = sgqlc.types.Field(String, graphql_name='title')
    cover_image = sgqlc.types.Field('IDInput', graphql_name='coverImage')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionType), graphql_name='type')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='app')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateMarketSolutionDetailInput)), graphql_name='detail')


class CreateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'permissions', 'desc')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PermissionInput')), graphql_name='permissions')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'name', 'company', 'department', 'role', 'phone', 'email', 'desc', 'is_active')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='role')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')


class DeleteCompaniesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteCompanyAdminUsersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteCompanyAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'app_ids')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')
    app_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='appIDs')


class DeleteDepartmentsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteUsersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DepartmentListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'ids', 'current_only', 'company')
    search = sgqlc.types.Field(String, graphql_name='search')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='ids')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class DepartmentNameSameAsSiblingsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='parent')


class DepartmentTreeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class ExportUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ForbiddenUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class GrantRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user_id', 'role_id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userId')
    role_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='roleId')


class IDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class IssueListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'status', 'category')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueStatus)), graphql_name='status')
    category = sgqlc.types.Field(sgqlc.types.non_null(IssueCategory), graphql_name='category')


class LoginInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class MarketAppFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_published', 'is_recommended', 'search', 'type')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    search = sgqlc.types.Field(String, graphql_name='search')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketAppType)), graphql_name='type')


class MarketCommonComponentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'content', 'image')
    title = sgqlc.types.Field(String, graphql_name='title')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field(IDInput, graphql_name='image')


class MarketIssueFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'type', 'status', 'search')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketConsultationType)), graphql_name='type')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketIssueStatus)), graphql_name='status')
    search = sgqlc.types.Field(String, graphql_name='search')


class MarketSolutionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_published', 'is_recommended', 'type', 'search')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketSolutionType)), graphql_name='type')
    search = sgqlc.types.Field(String, graphql_name='search')


class MyAppListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class MyCompanyAppFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class NotificationConfigFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('source_app', 'kind')
    source_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NotificationKind)), graphql_name='kind')


class NotificationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('source_app', 'is_read')
    source_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp')
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')


class PermissionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('permission', 'data_range')
    permission = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='permission')
    data_range = sgqlc.types.Field(PermissionDataRange, graphql_name='dataRange')


class PermissionListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('type', 'is_open', 'search')
    type = sgqlc.types.Field(PermissionType, graphql_name='type')
    is_open = sgqlc.types.Field(Boolean, graphql_name='isOpen')
    search = sgqlc.types.Field(String, graphql_name='search')


class PermissionTreeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'scope')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    scope = sgqlc.types.Field(String, graphql_name='scope')


class PlatformUserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('role', 'is_active', 'origin', 'search', 'role_code')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    origin = sgqlc.types.Field(UserOrigin, graphql_name='origin')
    search = sgqlc.types.Field(String, graphql_name='search')
    role_code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='roleCode')


class RegisterUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password', 'role_code')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    role_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='roleCode')


class ResetPasswordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user_ids',)
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userIDs')


class RestoreUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RoleExistsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class RoleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'search', 'company', 'scope', 'permission')
    id = sgqlc.types.Field(ID, graphql_name='id')
    search = sgqlc.types.Field(String, graphql_name='search')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    scope = sgqlc.types.Field(sgqlc.types.list_of(RoleScope), graphql_name='scope')
    permission = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permission')


class SystemLogFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'search', 'action', 'company')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    search = sgqlc.types.Field(String, graphql_name='search')
    action = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='action')
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class UpdateAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'kind', 'jump_kind', 'order', 'description', 'avatar', 'url', 'allowed_permissions', 'whether_new_client', 'redirect_url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(String, graphql_name='code')
    name = sgqlc.types.Field(String, graphql_name='name')
    kind = sgqlc.types.Field(AppKind, graphql_name='kind')
    jump_kind = sgqlc.types.Field(JumpKind, graphql_name='jumpKind')
    order = sgqlc.types.Field(Float, graphql_name='order')
    description = sgqlc.types.Field(String, graphql_name='description')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')
    url = sgqlc.types.Field(String, graphql_name='url')
    allowed_permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='allowedPermissions')
    whether_new_client = sgqlc.types.Field(Boolean, graphql_name='whetherNewClient')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')


class UpdateCompanyAdminUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'phone', 'email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')


class UpdateCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'address', 'uscc', 'contact', 'email', 'phone', 'province', 'city', 'county', 'company_type')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    address = sgqlc.types.Field(String, graphql_name='address')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')
    company_type = sgqlc.types.Field(IDInput, graphql_name='companyType')


class UpdateDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'parent', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent = sgqlc.types.Field(IDInput, graphql_name='parent')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'action', 'receiver', 'attachments', 'reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='id')
    remark = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='remark')
    action = sgqlc.types.Field(sgqlc.types.non_null(IssueAction), graphql_name='action')
    receiver = sgqlc.types.Field(IDInput, graphql_name='receiver')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachments')
    reason = sgqlc.types.Field(IssueReason, graphql_name='reason')


class UpdateMarketAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'type', 'cover_image', 'is_recommended', 'brief', 'description', 'screenshot')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(MarketAppType, graphql_name='type')
    cover_image = sgqlc.types.Field(IDInput, graphql_name='coverImage')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='screenshot')


class UpdateMarketIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'receiver', 'attachment', 'description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueAction), graphql_name='action')
    receiver = sgqlc.types.Field(IDInput, graphql_name='receiver')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachment')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class UpdateMarketSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'cover_image', 'type', 'is_recommended', 'brief', 'description', 'app', 'detail')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    cover_image = sgqlc.types.Field(IDInput, graphql_name='coverImage')
    type = sgqlc.types.Field(MarketSolutionType, graphql_name='type')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='app')
    detail = sgqlc.types.Field(sgqlc.types.list_of(CreateMarketSolutionDetailInput), graphql_name='detail')


class UpdateMeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('nickname', 'phone', 'email', 'avatar')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')


class UpdateMyCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'name', 'uscc', 'email', 'phone', 'province', 'city', 'county')
    address = sgqlc.types.Field(String, graphql_name='address')
    name = sgqlc.types.Field(String, graphql_name='name')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')


class UpdateMyPasswordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('old_password', 'new_password')
    old_password = sgqlc.types.Field(String, graphql_name='oldPassword')
    new_password = sgqlc.types.Field(String, graphql_name='newPassword')


class UpdateNotificationConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'to_inbox', 'to_email', 'receiver_user', 'receiver_role')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    to_inbox = sgqlc.types.Field(Boolean, graphql_name='toInbox')
    to_email = sgqlc.types.Field(Boolean, graphql_name='toEmail')
    receiver_user = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='receiverUser')
    receiver_role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='receiverRole')


class UpdateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'company', 'name', 'permissions', 'desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(String, graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionInput)), graphql_name='permissions')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'department', 'phone', 'email', 'role', 'desc', 'is_active')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')


class UserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids', 'company', 'department', 'role', 'is_active', 'search', 'current_only', 'type')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    search = sgqlc.types.Field(String, graphql_name='search')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserType)), graphql_name='type')


class companyExistsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'uscc')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class countryFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('full',)
    full = sgqlc.types.Field(Boolean, graphql_name='full')



########################################################################
# Output Objects and Interfaces
########################################################################
class App(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'key', 'kind', 'jump_kind', 'order', 'description', 'avatar', 'url', 'client_id', 'client_secret', 'redirect_url', 'allowed_permissions')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AppKind), graphql_name='kind')
    jump_kind = sgqlc.types.Field(sgqlc.types.non_null(JumpKind), graphql_name='jumpKind')
    order = sgqlc.types.Field(Float, graphql_name='order')
    description = sgqlc.types.Field(String, graphql_name='description')
    avatar = sgqlc.types.Field('Image', graphql_name='avatar')
    url = sgqlc.types.Field(String, graphql_name='url')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    client_secret = sgqlc.types.Field(String, graphql_name='clientSecret')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')
    allowed_permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Permission')), graphql_name='allowedPermissions')


class AppBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'datasource')
    app = sgqlc.types.Field(App, graphql_name='app')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BIDatasource'))), graphql_name='datasource')


class AppConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'icon_url', 'logo_url', 'public_url', 'route_url', 'hide_sidebar', 'entries')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    icon_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='iconUrl')
    logo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoUrl')
    public_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='publicUrl')
    route_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='routeUrl')
    hide_sidebar = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hideSidebar')
    entries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppEntry'))), graphql_name='entries')


class AppEntry(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('path', 'label', 'icon', 'children', 'permission_key', 'hidden')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    label = sgqlc.types.Field(String, graphql_name='label')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    children = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AppEntry')), graphql_name='children')
    permission_key = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permissionKey')
    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')


class AppList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AuthInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('token', 'user_id')
    token = sgqlc.types.Field(String, graphql_name='token')
    user_id = sgqlc.types.Field(String, graphql_name='userId')


class BIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'used')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    used = sgqlc.types.Field(Boolean, graphql_name='used')


class BIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'metric', 'value')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    value = sgqlc.types.Field(Float, graphql_name='value')


class City(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'counties')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('County')), graphql_name='counties')


class City_(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'province')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    province = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='province')


class Company(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'type', 'name', 'address', 'uscc', 'contact', 'email', 'phone', 'province', 'city', 'county', 'is_mine')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null('CompanyType'), graphql_name='type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    address = sgqlc.types.Field(String, graphql_name='address')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')
    is_mine = sgqlc.types.Field(Boolean, graphql_name='isMine')


class CompanyApps(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'apps')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    apps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='apps')


class CompanyAppsList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyApps)), graphql_name='data')


class CompanyBIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'app', 'datasource', 'created_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(BIDatasource), graphql_name='datasource')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')


class CompanyBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyBIDatasource)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CompanyTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Country(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'english', 'chinese', 'alpha2', 'alpha3')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    english = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='english')
    chinese = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chinese')
    alpha2 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha2')
    alpha3 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha3')


class County(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'companies')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')


class County_(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'city')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    city = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='city')


class Department(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'path_name', 'parent_id', 'is_deleted')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentID')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')


class DepartmentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class File(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'url', 'length')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    length = sgqlc.types.Field(Int, graphql_name='length')


class Image(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class Issue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'title', 'content', 'attachments', 'create_time', 'update_time', 'status', 'type', 'owner', 'issuer', 'company', 'logs')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachments')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createTime')
    update_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updateTime')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    type = sgqlc.types.Field(IssueType, graphql_name='type')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    issuer = sgqlc.types.Field('User', graphql_name='issuer')
    company = sgqlc.types.Field(Company, graphql_name='company')
    logs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLog')), graphql_name='logs')


class IssueList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count', 'ready', 'dealing', 'close')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Issue)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ready')
    dealing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dealing')
    close = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='close')


class IssueLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'action', 'remark', 'attachments', 'sender', 'receiver', 'reason')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    action = sgqlc.types.Field(IssueAction, graphql_name='action')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(File), graphql_name='attachments')
    sender = sgqlc.types.Field('User', graphql_name='sender')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    reason = sgqlc.types.Field(IssueReason, graphql_name='reason')


class MarketApp(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'type', 'published_at', 'updated_at', 'created_by', 'is_recommended', 'brief', 'description', 'cover_image', 'screenshot')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketAppType), graphql_name='type')
    published_at = sgqlc.types.Field(Timestamp, graphql_name='publishedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    cover_image = sgqlc.types.Field(File, graphql_name='coverImage')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='screenshot')


class MarketAppList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketApp)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketAppSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('published', 'draft', 'total')
    published = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='published')
    draft = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='draft')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class MarketCommonComponent(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('title', 'content', 'image')
    title = sgqlc.types.Field(String, graphql_name='title')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field(File, graphql_name='image')


class MarketIssue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'type', 'app', 'solution', 'created_at', 'updated_at', 'company_name', 'phone', 'email', 'contact', 'status', 'owner', 'content', 'issue_log')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(String, graphql_name='code')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketConsultationType), graphql_name='type')
    app = sgqlc.types.Field(MarketApp, graphql_name='app')
    solution = sgqlc.types.Field('MarketSolution', graphql_name='solution')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    status = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueStatus), graphql_name='status')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    issue_log = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketIssueLog')), graphql_name='issueLog')


class MarketIssueList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketIssue)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketIssueLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'operated_at', 'sender', 'receiver', 'description', 'attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueAction), graphql_name='action')
    operated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='operatedAt')
    sender = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='sender')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    description = sgqlc.types.Field(String, graphql_name='description')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachment')


class MarketIssueSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('ready', 'dealing', 'close')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ready')
    dealing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dealing')
    close = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='close')


class MarketSolution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'cover_image', 'type', 'is_recommended', 'brief', 'description', 'app', 'published_at', 'updated_at', 'created_by', 'detail')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    cover_image = sgqlc.types.Field(File, graphql_name='coverImage')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionType), graphql_name='type')
    is_recommended = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketApp)), graphql_name='app')
    published_at = sgqlc.types.Field(Timestamp, graphql_name='publishedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketSolutionDetail')), graphql_name='detail')


class MarketSolutionDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('title', 'items', 'image', 'content', 'type')
    title = sgqlc.types.Field(String, graphql_name='title')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketCommonComponent)), graphql_name='items')
    image = sgqlc.types.Field(File, graphql_name='image')
    content = sgqlc.types.Field(String, graphql_name='content')
    type = sgqlc.types.Field(sgqlc.types.non_null(CardType), graphql_name='type')


class MarketSolutionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketSolution)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketSolutionSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('published', 'draft', 'total')
    published = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='published')
    draft = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='draft')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class Mutation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('create_company', 'update_company', 'delete_companies', 'update_my_company', 'create_department', 'update_department', 'delete_department', 'create_company_bidatasource', 'delete_company_bidatasource', 'update_notification_config', 'read_notification', 'read_all_notification', 'create_file', 'create_files', 'create_image', 'create_images', 'create_market_file', 'create_market_files', 'create_role', 'update_role', 'delete_role', 'set_company_admin_permission', 'create_system_issue', 'update_system_issue', 'create_education_issue', 'update_education_issue', 'create_help_issue', 'update_help_issue', 'register_user', 'login', 'logout', 'create_company_admin_user', 'update_company_admin_user', 'delete_company_admin_users', 'create_user', 'update_user', 'import_user', 'delete_users', 'update_me', 'update_my_password', 'reset_password', 'restore_user', 'activate_user', 'forbidden_user', 'oauth_authorize', 'create_market_solution', 'update_market_solution', 'publish_market_solution', 'delete_market_solution', 'add_company_apps', 'delete_company_apps', 'visit_app', 'set_quick_access_app', 'create_app', 'update_app', 'set_third_party_app_permission', 'delete_app', 'set_workbench', 'create_market_app', 'update_market_app', 'publish_market_app', 'delete_market_app', 'create_market_issue', 'update_market_issue')
    create_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyInput), graphql_name='input', default=None)),
))
    )
    update_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCompanyInput), graphql_name='input', default=None)),
        ('scenario', sgqlc.types.Arg(UpdateCompanyScenario, graphql_name='scenario', default=None)),
))
    )
    delete_companies = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanies', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCompaniesInput), graphql_name='input', default=None)),
))
    )
    update_my_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMyCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateMyCompanyInput, graphql_name='input', default=None)),
))
    )
    create_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateDepartmentInput, graphql_name='input', default=None)),
))
    )
    update_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateDepartmentInput, graphql_name='input', default=None)),
))
    )
    delete_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyBIDatasourceInput), graphql_name='input', default=None)),
))
    )
    delete_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    update_notification_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateNotificationConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UpdateNotificationConfigInput))), graphql_name='input', default=None)),
))
    )
    read_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readNotification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    read_all_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readAllNotification', args=sgqlc.types.ArgDict((
        ('source_app', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp', default=None)),
))
    )
    create_file = sgqlc.types.Field(File, graphql_name='createFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    create_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateFileInput)), graphql_name='input', default=None)),
))
    )
    create_image = sgqlc.types.Field(Image, graphql_name='createImage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateImageInput), graphql_name='input', default=None)),
))
    )
    create_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Image)), graphql_name='createImages', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateImageInput)), graphql_name='input', default=None)),
))
    )
    create_market_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createMarketFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketFileInput), graphql_name='input', default=None)),
))
    )
    create_market_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createMarketFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateMarketFileInput)), graphql_name='input', default=None)),
))
    )
    create_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRoleInput), graphql_name='input', default=None)),
))
    )
    update_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRoleInput), graphql_name='input', default=None)),
))
    )
    delete_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRole', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    set_company_admin_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyAdminPermission', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CompanyAdminPermissionInput, graphql_name='input', default=None)),
))
    )
    create_system_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createSystemIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    update_system_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateSystemIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    create_education_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createEducationIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    update_education_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateEducationIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    create_help_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createHelpIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    update_help_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateHelpIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    register_user = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='registerUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(RegisterUserInput, graphql_name='input', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='login', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginInput), graphql_name='input', default=None)),
))
    )
    logout = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='logout')
    create_company_admin_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createCompanyAdminUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateCompanyAdminUserInput, graphql_name='input', default=None)),
))
    )
    update_company_admin_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompanyAdminUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateCompanyAdminUserInput, graphql_name='input', default=None)),
))
    )
    delete_company_admin_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyAdminUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(DeleteCompanyAdminUsersInput, graphql_name='input', default=None)),
))
    )
    create_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='input', default=None)),
))
    )
    update_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='input', default=None)),
))
    )
    import_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    delete_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUsersInput), graphql_name='input', default=None)),
))
    )
    update_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMe', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMeInput), graphql_name='input', default=None)),
))
    )
    update_my_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMyPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateMyPasswordInput, graphql_name='input', default=None)),
))
    )
    reset_password = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='resetPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ResetPasswordInput, graphql_name='input', default=None)),
        ('scenario', sgqlc.types.Arg(ResetPasswordScenario, graphql_name='scenario', default=None)),
))
    )
    restore_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restoreUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestoreUserInput), graphql_name='input', default=None)),
))
    )
    activate_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ActivateUserInput), graphql_name='input', default=None)),
))
    )
    forbidden_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='forbiddenUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ForbiddenUserInput), graphql_name='input', default=None)),
))
    )
    oauth_authorize = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oauthAuthorize', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
        ('nonce', sgqlc.types.Arg(String, graphql_name='nonce', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    create_market_solution = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createMarketSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketSolutionInput), graphql_name='input', default=None)),
))
    )
    update_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketSolutionInput), graphql_name='input', default=None)),
))
    )
    publish_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishMarketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMarketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    add_company_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addCompanyApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddCompanyAppsInput), graphql_name='input', default=None)),
))
    )
    delete_company_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCompanyAppsInput), graphql_name='input', default=None)),
))
    )
    visit_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visitApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    set_quick_access_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setQuickAccessApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_app = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAppInput), graphql_name='input', default=None)),
))
    )
    update_app = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='updateApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAppInput), graphql_name='input', default=None)),
))
    )
    set_third_party_app_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThirdPartyAppPermission', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='appID', default=None)),
        ('permission', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='permission', default=None)),
))
    )
    delete_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='deleteApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    set_workbench = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setWorkbench', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='input', default=None)),
))
    )
    create_market_app = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createMarketApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketAppInput), graphql_name='input', default=None)),
))
    )
    update_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketAppInput), graphql_name='input', default=None)),
))
    )
    publish_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishMarketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMarketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_market_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createMarketIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketIssueInput), graphql_name='input', default=None)),
))
    )
    update_market_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketIssueInput), graphql_name='input', default=None)),
))
    )


class Notification(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'kind', 'source_app', 'content', 'created_at', 'is_read', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    kind = sgqlc.types.Field(sgqlc.types.non_null(NotificationKind), graphql_name='kind')
    source_app = sgqlc.types.Field(App, graphql_name='sourceApp')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    url = sgqlc.types.Field(String, graphql_name='url')


class NotificationConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'source_app', 'description', 'to_inbox', 'to_email', 'receiver_user', 'receiver_role', 'template', 'kind')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    source_app = sgqlc.types.Field(App, graphql_name='sourceApp')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    to_inbox = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toInbox')
    to_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toEmail')
    receiver_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='receiverUser')
    receiver_role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Role'))), graphql_name='receiverRole')
    template = sgqlc.types.Field(sgqlc.types.non_null('NotificationTemplate'), graphql_name='template')
    kind = sgqlc.types.Field(sgqlc.types.non_null(NotificationKind), graphql_name='kind')


class NotificationConfigList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NotificationConfig))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class NotificationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count', 'read_count', 'unread_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Notification))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    read_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='readCount')
    unread_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unreadCount')


class NotificationTemplate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('inbox', 'email')
    inbox = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inbox')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')


class Permission(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'desc', 'code', 'weakrefs', 'type', 'is_open', 'range')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    weakrefs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='weakrefs')
    type = sgqlc.types.Field(sgqlc.types.non_null(PermissionType), graphql_name='type')
    is_open = sgqlc.types.Field(Boolean, graphql_name='isOpen')
    range = sgqlc.types.Field(PermissionDataRange, graphql_name='range')


class PermissionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Province(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Query(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company_exists', 'company_type_list', 'countries', 'provinces', 'cities', 'counties', 'company', 'companies', 'city_companies', 'type_companies', 'my_company', 'department_tree', 'department_list', 'department_name_same_as_siblings', 'company_bidatasource_list', 'company_bidatasource_tree', 'notification_config_list', 'notification_config', 'notification_list', 'notification', 'notification_config_app', 'notification_app', 'upload_config', 'upload_configs', 'role_list', 'permission_tree', 'permission_list', 'role_exists', 'issues', 'export_issues', 'issue', 'account_exists', 'me', 'company_admin_users', 'platform_admin_users', 'users', 'platform_user_list', 'user', 'user_template', 'export_user', 'support_users', 'app_users', 'oauth_permission_list', 'market_solution_list', 'market_solution', 'market_solution_summary', 'app_list', 'app', 'company_apps', 'my_company_apps', 'my_app_list', 'quick_access_app', 'recent_app', 'app_config', 'workbench', 'workbench_card_option', 'workbench_card_data', 'system_log_list', 'system_log_action', 'market_app_list', 'market_app', 'market_app_summary', 'market_issue_list', 'market_issue', 'market_issue_summary', 'bi_issue_issue', '_service', '_entities')
    company_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='companyExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(companyExistsFilter), graphql_name='filter', default=None)),
))
    )
    company_type_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyTypeList), graphql_name='companyTypeList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(CompanyTypeFilter, graphql_name='filter', default=None)),
))
    )
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Country)), graphql_name='countries', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(countryFilter, graphql_name='filter', default=None)),
))
    )
    provinces = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Province)), graphql_name='provinces')
    cities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City_)), graphql_name='cities', args=sgqlc.types.ArgDict((
        ('province_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='provinceID', default=None)),
))
    )
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(County_)), graphql_name='counties', args=sgqlc.types.ArgDict((
        ('city_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='cityID', default=None)),
))
    )
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    companies = sgqlc.types.Field(sgqlc.types.non_null(CompanyList), graphql_name='companies', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyFilter, graphql_name='filter', default=None)),
))
    )
    city_companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City)), graphql_name='cityCompanies')
    type_companies = sgqlc.types.Field(sgqlc.types.non_null('TypeCompaniesList'), graphql_name='typeCompanies', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyFilter, graphql_name='filter', default=None)),
        ('scenario', sgqlc.types.Arg(TypeCompaniesScenario, graphql_name='scenario', default=None)),
))
    )
    my_company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='myCompany')
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentTreeFilter, graphql_name='filter', default=None)),
))
    )
    department_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='departmentList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DepartmentListFilter), graphql_name='filter', default=None)),
))
    )
    department_name_same_as_siblings = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='departmentNameSameAsSiblings', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DepartmentNameSameAsSiblingsFilter), graphql_name='filter', default=None)),
))
    )
    company_bidatasource_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyBIDatasourceList), graphql_name='companyBIDatasourceList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
))
    )
    company_bidatasource_tree = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AppBIDatasourceList)), graphql_name='companyBIDatasourceTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
))
    )
    notification_config_list = sgqlc.types.Field(sgqlc.types.non_null(NotificationConfigList), graphql_name='notificationConfigList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(NotificationConfigFilterInput, graphql_name='filter', default=None)),
))
    )
    notification_config = sgqlc.types.Field(sgqlc.types.non_null(NotificationConfig), graphql_name='notificationConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    notification_list = sgqlc.types.Field(sgqlc.types.non_null(NotificationList), graphql_name='notificationList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(NotificationFilterInput, graphql_name='filter', default=None)),
))
    )
    notification = sgqlc.types.Field(sgqlc.types.non_null(Notification), graphql_name='notification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    notification_config_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='notificationConfigApp')
    notification_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='notificationApp')
    upload_config = sgqlc.types.Field('UploadConfig', graphql_name='uploadConfig', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    upload_configs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UploadConfig')), graphql_name='uploadConfigs', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='names', default=None)),
))
    )
    role_list = sgqlc.types.Field(sgqlc.types.non_null('RoleList'), graphql_name='roleList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RoleFilterInput, graphql_name='filter', default=None)),
))
    )
    permission_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='permissionTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionTreeFilterInput, graphql_name='filter', default=None)),
))
    )
    permission_list = sgqlc.types.Field(sgqlc.types.non_null(PermissionList), graphql_name='permissionList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(PermissionListFilterInput, graphql_name='filter', default=None)),
))
    )
    role_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='roleExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RoleExistsFilterInput, graphql_name='filter', default=None)),
))
    )
    issues = sgqlc.types.Field(IssueList, graphql_name='issues', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('filter', sgqlc.types.Arg(IssueListFilter, graphql_name='filter', default=None)),
        ('mine_only', sgqlc.types.Arg(Boolean, graphql_name='mineOnly', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_issues = sgqlc.types.Field('RawFile', graphql_name='exportIssues', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('filter', sgqlc.types.Arg(IssueListFilter, graphql_name='filter', default=None)),
        ('mine_only', sgqlc.types.Arg(Boolean, graphql_name='mineOnly', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    issue = sgqlc.types.Field(Issue, graphql_name='issue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    account_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='accountExists', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account', default=None)),
))
    )
    me = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='me')
    company_admin_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='companyAdminUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyAdminUsersFilter, graphql_name='filter', default=None)),
))
    )
    platform_admin_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='platformAdminUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(UserListFilter, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    platform_user_list = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='platformUserList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(PlatformUserListFilter, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    user_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='userTemplate')
    export_user = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportUserInput, graphql_name='input', default=None)),
))
    )
    support_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='supportUsers')
    app_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='appUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(AppUserListFilter, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    oauth_permission_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Permission)), graphql_name='oauthPermissionList', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
))
    )
    market_solution_list = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionList), graphql_name='marketSolutionList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(MarketSolutionFilterInput, graphql_name='filter', default=None)),
))
    )
    market_solution = sgqlc.types.Field(sgqlc.types.non_null(MarketSolution), graphql_name='marketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_solution_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionSummary), graphql_name='marketSolutionSummary')
    app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='appList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(AppListFilter, graphql_name='filter', default=None)),
))
    )
    app = sgqlc.types.Field(App, graphql_name='app', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    company_apps = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='companyApps', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyAppsFilter, graphql_name='filter', default=None)),
))
    )
    my_company_apps = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myCompanyApps', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(MyCompanyAppFilter, graphql_name='filter', default=None)),
))
    )
    my_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myAppList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(MyAppListFilter, graphql_name='filter', default=None)),
))
    )
    quick_access_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='quickAccessApp')
    recent_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='recentApp', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    app_config = sgqlc.types.Field(sgqlc.types.non_null(AppConfig), graphql_name='appConfig', args=sgqlc.types.ArgDict((
        ('app_code', sgqlc.types.Arg(String, graphql_name='appCode', default='main')),
))
    )
    workbench = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbench')
    workbench_card_option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbenchCardOption')
    workbench_card_data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='workbenchCardData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    system_log_list = sgqlc.types.Field(sgqlc.types.non_null('SystemLogList'), graphql_name='systemLogList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SystemLogFilterInput), graphql_name='filter', default=None)),
))
    )
    system_log_action = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='systemLogAction', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyId', default=None)),
))
    )
    market_app_list = sgqlc.types.Field(sgqlc.types.non_null(MarketAppList), graphql_name='marketAppList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(MarketAppFilterInput, graphql_name='filter', default=None)),
))
    )
    market_app = sgqlc.types.Field(sgqlc.types.non_null(MarketApp), graphql_name='marketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_app_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketAppSummary), graphql_name='marketAppSummary')
    market_issue_list = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueList), graphql_name='marketIssueList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MarketIssueFilterInput), graphql_name='filter', default=None)),
))
    )
    market_issue = sgqlc.types.Field(sgqlc.types.non_null(MarketIssue), graphql_name='marketIssue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_issue_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueSummary), graphql_name='marketIssueSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MarketIssueFilterInput), graphql_name='filter', default=None)),
))
    )
    bi_issue_issue = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biIssueIssue', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    _service = sgqlc.types.Field(sgqlc.types.non_null('_Service'), graphql_name='_service')
    _entities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('_Entity')), graphql_name='_entities', args=sgqlc.types.ArgDict((
        ('representations', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(_Any))), graphql_name='representations', default=None)),
))
    )


class RawFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'name')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')
    name = sgqlc.types.Field(String, graphql_name='name')


class Role(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'permissions', 'desc', 'updated_at', 'created_at', 'app')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='permissions')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(App)), graphql_name='app')


class RoleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SystemLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'user', 'timestamp', 'action', 'resource', 'app')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field('User', graphql_name='user')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    resource = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resource')
    app = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='app')


class SystemLogList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SystemLog))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TypeCompanies(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type', 'companies')
    type = sgqlc.types.Field(sgqlc.types.non_null(CompanyType), graphql_name='type')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')


class TypeCompaniesList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TypeCompanies)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UploadConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('url', 'name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class User(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'account', 'name', 'company', 'department', 'password', 'nickname', 'phone', 'email', 'avatar', 'desc', 'type', 'counties', 'role', 'is_active', 'create_time', 'update_time', 'origin', 'is_mine')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field(Company, graphql_name='company')
    department = sgqlc.types.Field(Department, graphql_name='department')
    password = sgqlc.types.Field(String, graphql_name='password')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    type = sgqlc.types.Field(sgqlc.types.non_null(UserType), graphql_name='type')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='counties')
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='role')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createTime')
    update_time = sgqlc.types.Field(Timestamp, graphql_name='updateTime')
    origin = sgqlc.types.Field(UserOrigin, graphql_name='origin')
    is_mine = sgqlc.types.Field(Boolean, graphql_name='isMine')


class UserList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(User)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkbenchCard(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class _Service(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('sdl',)
    sdl = sgqlc.types.Field(String, graphql_name='sdl')



########################################################################
# Unions
########################################################################
class _Entity(sgqlc.types.Union):
    __schema__ = platform_schema
    __types__ = (Company, Department, BIDatasource, Image, Role, User)



########################################################################
# Schema Entry Points
########################################################################
platform_schema.query_type = Query
platform_schema.mutation_type = Mutation
platform_schema.subscription_type = None

