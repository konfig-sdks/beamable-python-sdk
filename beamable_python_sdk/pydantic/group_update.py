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


class GroupUpdate(BaseModel):
    name: typing.Optional[str] = Field(None, alias='name')

    enrollment_type: typing.Optional[str] = Field(None, alias='enrollmentType')

    tag: typing.Optional[str] = Field(None, alias='tag')

    slogan: typing.Optional[str] = Field(None, alias='slogan')

    requirement: typing.Optional[int] = Field(None, alias='requirement')

    motd: typing.Optional[str] = Field(None, alias='motd')

    client_data: typing.Optional[str] = Field(None, alias='clientData')

    sub_group: typing.Optional[int] = Field(None, alias='subGroup')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
