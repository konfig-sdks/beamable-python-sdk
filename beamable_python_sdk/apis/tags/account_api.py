# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.basic_accounts_available_device_id.get import CheckAvailability
from beamable_python_sdk.paths.basic_accounts_available.get import CheckAvailability0
from beamable_python_sdk.paths.basic_accounts_available_third_party.get import CheckThirdPartyAvailability
from beamable_python_sdk.paths.basic_accounts_admin_admin_user.post import CreateAdminUser
from beamable_python_sdk.paths.object_accounts_object_id_admin_scope.delete import DeleteAdminScope
from beamable_python_sdk.paths.basic_accounts_me_third_party.delete import DeleteThirdParty
from beamable_python_sdk.paths.object_accounts_object_id_admin_third_party.delete import DeleteThirdPartyAdmin
from beamable_python_sdk.paths.basic_accounts_find.get import FindAccounts
from beamable_python_sdk.paths.basic_accounts_admin_admin_users.get import GetAdminUsers
from beamable_python_sdk.paths.basic_accounts_admin_me.get import GetDetails
from beamable_python_sdk.paths.object_accounts_object_id_available_roles.get import GetObjectAvailableRoles
from beamable_python_sdk.paths.basic_accounts_get_personally_identifiable_information.get import GetPersonallyIdentifiableInformation
from beamable_python_sdk.paths.basic_accounts_me.get import GetUserInfo
from beamable_python_sdk.paths.basic_history_account_roles.get import ListRoles
from beamable_python_sdk.paths.basic_accounts_register.post import RegisterNewAccount
from beamable_python_sdk.paths.object_accounts_object_id_admin_forget.delete import RemoveAdminForget
from beamable_python_sdk.paths.basic_accounts_me_device.delete import RemoveDevice
from beamable_python_sdk.paths.object_accounts_object_id_role.delete import RemoveRole
from beamable_python_sdk.paths.basic_accounts_search.get import SearchAccounts
from beamable_python_sdk.paths.basic_accounts_me.put import UpdateAccountInfo
from beamable_python_sdk.paths.object_accounts_object_id_admin_scope.put import UpdateAdminScope
from beamable_python_sdk.paths.basic_accounts_password_update_confirm.post import UpdatePasswordConfirmation
from beamable_python_sdk.paths.basic_accounts_password_update_init.post import UpdatePasswordInit
from beamable_python_sdk.paths.object_accounts_object_id_role.put import UpdateRole
from beamable_python_sdk.paths.object_accounts_object_id_admin_third_party.put import UpdateThirdPartyAdmin
from beamable_python_sdk.apis.tags.account_api_raw import AccountApiRaw


class AccountApi(
    CheckAvailability,
    CheckAvailability0,
    CheckThirdPartyAvailability,
    CreateAdminUser,
    DeleteAdminScope,
    DeleteThirdParty,
    DeleteThirdPartyAdmin,
    FindAccounts,
    GetAdminUsers,
    GetDetails,
    GetObjectAvailableRoles,
    GetPersonallyIdentifiableInformation,
    GetUserInfo,
    ListRoles,
    RegisterNewAccount,
    RemoveAdminForget,
    RemoveDevice,
    RemoveRole,
    SearchAccounts,
    UpdateAccountInfo,
    UpdateAdminScope,
    UpdatePasswordConfirmation,
    UpdatePasswordInit,
    UpdateRole,
    UpdateThirdPartyAdmin,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AccountApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AccountApiRaw(api_client)
