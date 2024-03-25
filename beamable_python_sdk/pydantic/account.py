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

from beamable_python_sdk.pydantic.account_device_ids import AccountDeviceIds
from beamable_python_sdk.pydantic.account_projects import AccountProjects
from beamable_python_sdk.pydantic.gamer_tag_association import GamerTagAssociation
from beamable_python_sdk.pydantic.in_flight_message import InFlightMessage
from beamable_python_sdk.pydantic.role_mapping import RoleMapping
from beamable_python_sdk.pydantic.third_party_association import ThirdPartyAssociation

class Account(BaseModel):
    password: str = Field(alias='password')

    user: str = Field(alias='user')

    projects: AccountProjects = Field(alias='projects')

    in_flight: typing.Optional[typing.List[InFlightMessage]] = Field(None, alias='inFlight')

    created_time_millis: typing.Optional[int] = Field(None, alias='createdTimeMillis')

    realm_id: typing.Optional[str] = Field(None, alias='realmId')

    email: typing.Optional[str] = Field(None, alias='email')

    role_string: typing.Optional[str] = Field(None, alias='roleString')

    device_ids: typing.Optional[AccountDeviceIds] = Field(None, alias='deviceIds')

    privileged_account: typing.Optional[bool] = Field(None, alias='privilegedAccount')

    country: typing.Optional[str] = Field(None, alias='country')

    was_migrated: typing.Optional[bool] = Field(None, alias='wasMigrated')

    id: typing.Optional[int] = Field(None, alias='id')

    gamer_tags: typing.Optional[typing.List[GamerTagAssociation]] = Field(None, alias='gamerTags')

    language: typing.Optional[str] = Field(None, alias='language')

    roles: typing.Optional[typing.List[RoleMapping]] = Field(None, alias='roles')

    updated_time_millis: typing.Optional[int] = Field(None, alias='updatedTimeMillis')

    third_parties: typing.Optional[typing.List[ThirdPartyAssociation]] = Field(None, alias='thirdParties')

    device_id: typing.Optional[str] = Field(None, alias='deviceId')

    user_name: typing.Optional[str] = Field(None, alias='userName')

    heartbeat: typing.Optional[int] = Field(None, alias='heartbeat')

    created: typing.Optional[int] = Field(None, alias='created')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
