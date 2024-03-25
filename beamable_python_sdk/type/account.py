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

from beamable_python_sdk.type.account_device_ids import AccountDeviceIds
from beamable_python_sdk.type.account_projects import AccountProjects
from beamable_python_sdk.type.gamer_tag_association import GamerTagAssociation
from beamable_python_sdk.type.in_flight_message import InFlightMessage
from beamable_python_sdk.type.role_mapping import RoleMapping
from beamable_python_sdk.type.third_party_association import ThirdPartyAssociation

class RequiredAccount(TypedDict):
    password: str

    user: str

    projects: AccountProjects

class OptionalAccount(TypedDict, total=False):
    inFlight: typing.List[InFlightMessage]

    createdTimeMillis: int

    realmId: str

    email: str

    roleString: str

    deviceIds: AccountDeviceIds

    privilegedAccount: bool

    country: str

    wasMigrated: bool

    id: int

    gamerTags: typing.List[GamerTagAssociation]

    language: str

    roles: typing.List[RoleMapping]

    updatedTimeMillis: int

    thirdParties: typing.List[ThirdPartyAssociation]

    deviceId: str

    userName: str

    heartbeat: int

    created: int

class Account(RequiredAccount, OptionalAccount):
    pass
