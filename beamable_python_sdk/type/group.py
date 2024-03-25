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

from beamable_python_sdk.type.donation_request import DonationRequest
from beamable_python_sdk.type.group_maybe_donations import GroupMaybeDonations
from beamable_python_sdk.type.group_role import GroupRole
from beamable_python_sdk.type.group_scores import GroupScores
from beamable_python_sdk.type.in_flight_message import InFlightMessage
from beamable_python_sdk.type.member import Member

class RequiredGroup(TypedDict):
    freeSlots: int

    leader: int

    requirement: int

    id: int

    maxSize: int

class OptionalGroup(TypedDict, total=False):
    version: int

    inFlight: typing.List[InFlightMessage]

    name: str

    enrollmentType: str

    donations: typing.List[DonationRequest]

    maybeDonations: GroupMaybeDonations

    tag: str

    canUpdateMOTD: bool

    shard: str

    canUpdateSlogan: bool

    slogan: str

    motd: str

    clientData: str

    roles: typing.List[GroupRole]

    scores: GroupScores

    canUpdateEnrollment: bool

    members: typing.List[Member]

    canDisband: bool

    type: str

    subGroups: 'typing.List["Group"]'

    created: int

class Group(RequiredGroup, OptionalGroup):
    pass
