# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from beamable_python_sdk.type.group_membership_response_sub_groups import GroupMembershipResponseSubGroups
from beamable_python_sdk.type.group_meta_data import GroupMetaData

class RequiredGroupMembershipResponse(TypedDict):
    member: bool

class OptionalGroupMembershipResponse(TypedDict, total=False):
    gamerTag: int

    type: str

    subGroups: GroupMembershipResponseSubGroups

    group: GroupMetaData

class GroupMembershipResponse(RequiredGroupMembershipResponse, OptionalGroupMembershipResponse):
    pass
