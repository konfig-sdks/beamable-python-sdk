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

from beamable_python_sdk.pydantic.donation_request import DonationRequest
from beamable_python_sdk.pydantic.group_maybe_donations import GroupMaybeDonations
from beamable_python_sdk.pydantic.group_role import GroupRole
from beamable_python_sdk.pydantic.group_scores import GroupScores
from beamable_python_sdk.pydantic.in_flight_message import InFlightMessage
from beamable_python_sdk.pydantic.member import Member

class Group(BaseModel):
    free_slots: int = Field(alias='freeSlots')

    leader: int = Field(alias='leader')

    requirement: int = Field(alias='requirement')

    id: int = Field(alias='id')

    max_size: int = Field(alias='maxSize')

    version: typing.Optional[int] = Field(None, alias='version')

    in_flight: typing.Optional[typing.List[InFlightMessage]] = Field(None, alias='inFlight')

    name: typing.Optional[str] = Field(None, alias='name')

    enrollment_type: typing.Optional[str] = Field(None, alias='enrollmentType')

    donations: typing.Optional[typing.List[DonationRequest]] = Field(None, alias='donations')

    maybe_donations: typing.Optional[GroupMaybeDonations] = Field(None, alias='maybeDonations')

    tag: typing.Optional[str] = Field(None, alias='tag')

    can_update_m_o_t_d: typing.Optional[bool] = Field(None, alias='canUpdateMOTD')

    shard: typing.Optional[str] = Field(None, alias='shard')

    can_update_slogan: typing.Optional[bool] = Field(None, alias='canUpdateSlogan')

    slogan: typing.Optional[str] = Field(None, alias='slogan')

    motd: typing.Optional[str] = Field(None, alias='motd')

    client_data: typing.Optional[str] = Field(None, alias='clientData')

    roles: typing.Optional[typing.List[GroupRole]] = Field(None, alias='roles')

    scores: typing.Optional[GroupScores] = Field(None, alias='scores')

    can_update_enrollment: typing.Optional[bool] = Field(None, alias='canUpdateEnrollment')

    members: typing.Optional[typing.List[Member]] = Field(None, alias='members')

    can_disband: typing.Optional[bool] = Field(None, alias='canDisband')

    type: typing.Optional[Literal["not-available"]] = Field(None, alias='type')

    sub_groups: typing.Optional['typing.List["Group"]'] = Field(None, alias='subGroups')

    created: typing.Optional[int] = Field(None, alias='created')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
