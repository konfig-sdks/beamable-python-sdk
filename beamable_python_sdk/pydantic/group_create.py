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

class GroupCreate(BaseModel):
    requirement: int = Field(alias='requirement')

    max_size: int = Field(alias='maxSize')

    name: typing.Optional[str] = Field(None, alias='name')

    enrollment_type: typing.Optional[str] = Field(None, alias='enrollmentType')

    tag: typing.Optional[str] = Field(None, alias='tag')

    client_data: typing.Optional[str] = Field(None, alias='clientData')

    scores: typing.Optional[typing.List[GroupScoreBinding]] = Field(None, alias='scores')

    time: typing.Optional[int] = Field(None, alias='time')

    type: typing.Optional[Literal["not-available"]] = Field(None, alias='type')

    group: typing.Optional[int] = Field(None, alias='group')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
