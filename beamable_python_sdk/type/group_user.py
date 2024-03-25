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

from beamable_python_sdk.type.group_score_binding import GroupScoreBinding
from beamable_python_sdk.type.group_user_member import GroupUserMember
from beamable_python_sdk.type.in_flight_message import InFlightMessage

class RequiredGroupUser(TypedDict):
    gamerTag: int

class OptionalGroupUser(TypedDict, total=False):
    inFlight: typing.List[InFlightMessage]

    allGroups: typing.List[GroupUserMember]

    updated: int

    member: GroupUserMember

    scores: typing.List[GroupScoreBinding]

class GroupUser(RequiredGroupUser, OptionalGroupUser):
    pass
