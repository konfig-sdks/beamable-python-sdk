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

from beamable_python_sdk.pydantic.group_membership_response_sub_groups import GroupMembershipResponseSubGroups
from beamable_python_sdk.pydantic.group_meta_data import GroupMetaData

class GroupMembershipResponse(BaseModel):
    member: bool = Field(alias='member')

    gamer_tag: typing.Optional[int] = Field(None, alias='gamerTag')

    type: typing.Optional[Literal["not-available"]] = Field(None, alias='type')

    sub_groups: typing.Optional[GroupMembershipResponseSubGroups] = Field(None, alias='subGroups')

    group: typing.Optional[GroupMetaData] = Field(None, alias='group')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
