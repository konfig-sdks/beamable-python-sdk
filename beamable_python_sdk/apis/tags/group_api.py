# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.object_groups_object_id_apply.post import ApplyObjectGroups
from beamable_python_sdk.paths.object_group_users_object_id_group.post import AssignObjectGroup
from beamable_python_sdk.paths.object_groups_object_id_donations.post import CreateDonation
from beamable_python_sdk.paths.object_groups_object_id_petition.post import CreatePetition
from beamable_python_sdk.paths.object_groups_object_id.delete import DeleteObjectGroup
from beamable_python_sdk.paths.object_group_users_object_id.get import GetGroupUsers
from beamable_python_sdk.paths.object_groups_object_id.get import GetObjectGroups
from beamable_python_sdk.paths.object_group_users_object_id_recommended.get import GetRecommendedUsers
from beamable_python_sdk.paths.object_group_users_object_id_availability.get import GetUserAvailability
from beamable_python_sdk.paths.object_groups_object_id_invite.post import InviteObjectGroup
from beamable_python_sdk.paths.object_group_users_object_id_join.delete import JoinUserDelete
from beamable_python_sdk.paths.object_group_users_object_id_join.post import JoinUserToGroup
from beamable_python_sdk.paths.object_groups_object_id_kick.post import KickObjectGroup
from beamable_python_sdk.paths.object_groups_object_id_member.delete import RemoveMember
from beamable_python_sdk.paths.basic_groups_search.get import SearchGroups
from beamable_python_sdk.paths.object_group_users_object_id_search.get import SearchUsers
from beamable_python_sdk.paths.object_groups_object_id_donations.put import UpdateDonation
from beamable_python_sdk.paths.object_groups_object_id.put import UpdateObjectGroup
from beamable_python_sdk.paths.object_groups_object_id_role.put import UpdateRole
from beamable_python_sdk.apis.tags.group_api_raw import GroupApiRaw


class GroupApi(
    ApplyObjectGroups,
    AssignObjectGroup,
    CreateDonation,
    CreatePetition,
    DeleteObjectGroup,
    GetGroupUsers,
    GetObjectGroups,
    GetRecommendedUsers,
    GetUserAvailability,
    InviteObjectGroup,
    JoinUserDelete,
    JoinUserToGroup,
    KickObjectGroup,
    RemoveMember,
    SearchGroups,
    SearchUsers,
    UpdateDonation,
    UpdateObjectGroup,
    UpdateRole,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GroupApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GroupApiRaw(api_client)
