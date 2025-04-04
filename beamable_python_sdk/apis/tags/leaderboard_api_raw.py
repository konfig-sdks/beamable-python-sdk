# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.object_leaderboards_object_id_freeze.put import CreateFreezeRequestRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_entries.delete import DeleteEntriesRaw
from beamable_python_sdk.paths.object_leaderboards_object_id.delete import DeleteObjectByIdRaw
from beamable_python_sdk.paths.basic_leaderboards_assignment.get import GetAssignmentLeaderboardRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_details.get import GetObjectDetailsRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_matches.get import GetObjectMatchesRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_membership.get import GetObjectMembershipRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_partition.get import GetObjectPartitionRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_view.get import GetObjectViewRaw
from beamable_python_sdk.paths.basic_leaderboards_player.get import GetPlayerScoresRaw
from beamable_python_sdk.paths.basic_leaderboards_uid.get import GetUserScoresRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_ranks.get import ListObjectRanksRaw
from beamable_python_sdk.paths.basic_leaderboards_list.get import ListUserScoresRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_assignment.delete import RemoveAssignmentRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_entry.delete import RemoveEntryRaw
from beamable_python_sdk.paths.object_leaderboards_object_id.post import SubmitObjectScoresRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_swap.put import SwapObjectLeaderboardRaw
from beamable_python_sdk.paths.object_leaderboards_object_id_entry.put import UpdateEntryRaw


class LeaderboardApiRaw(
    CreateFreezeRequestRaw,
    DeleteEntriesRaw,
    DeleteObjectByIdRaw,
    GetAssignmentLeaderboardRaw,
    GetObjectDetailsRaw,
    GetObjectMatchesRaw,
    GetObjectMembershipRaw,
    GetObjectPartitionRaw,
    GetObjectViewRaw,
    GetPlayerScoresRaw,
    GetUserScoresRaw,
    ListObjectRanksRaw,
    ListUserScoresRaw,
    RemoveAssignmentRaw,
    RemoveEntryRaw,
    SubmitObjectScoresRaw,
    SwapObjectLeaderboardRaw,
    UpdateEntryRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
