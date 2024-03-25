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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from beamable_python_sdk.pydantic.group_score_binding import GroupScoreBinding
from beamable_python_sdk.pydantic.group_user_member import GroupUserMember
from beamable_python_sdk.pydantic.in_flight_message import InFlightMessage

class GroupUser(BaseModel):
    gamer_tag: int = Field(alias='gamerTag')

    in_flight: typing.Optional[typing.List[InFlightMessage]] = Field(None, alias='inFlight')

    all_groups: typing.Optional[typing.List[GroupUserMember]] = Field(None, alias='allGroups')

    updated: typing.Optional[int] = Field(None, alias='updated')

    member: typing.Optional[GroupUserMember] = Field(None, alias='member')

    scores: typing.Optional[typing.List[GroupScoreBinding]] = Field(None, alias='scores')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
