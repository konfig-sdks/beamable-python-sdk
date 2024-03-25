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


class GroupMembershipRequest(BaseModel):
    group: int = Field(alias='group')

    successor: typing.Optional[int] = Field(None, alias='successor')

    score: typing.Optional[int] = Field(None, alias='score')

    sub_group: typing.Optional[int] = Field(None, alias='subGroup')

    type: typing.Optional[Literal["not-available"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
