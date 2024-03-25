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


class GroupSearchRequest(BaseModel):
    name: typing.Optional[str] = Field(None, alias='name')

    score_min: typing.Optional[int] = Field(None, alias='scoreMin')

    sort_field: typing.Optional[str] = Field(None, alias='sortField')

    user_score: typing.Optional[int] = Field(None, alias='userScore')

    has_slots: typing.Optional[bool] = Field(None, alias='hasSlots')

    enrollment_types: typing.Optional[str] = Field(None, alias='enrollmentTypes')

    offset: typing.Optional[int] = Field(None, alias='offset')

    score_max: typing.Optional[int] = Field(None, alias='scoreMax')

    sub_group: typing.Optional[bool] = Field(None, alias='subGroup')

    sort_value: typing.Optional[int] = Field(None, alias='sortValue')

    type: typing.Optional[Literal["not-available"]] = Field(None, alias='type')

    limit: typing.Optional[int] = Field(None, alias='limit')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
