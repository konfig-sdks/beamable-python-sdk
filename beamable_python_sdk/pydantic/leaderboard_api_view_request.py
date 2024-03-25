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


class LeaderboardApiViewRequest(BaseModel):
    max: typing.Optional[int] = Field(None, alias='max')

    focus: typing.Optional[int] = Field(None, alias='focus')

    friends: typing.Optional[bool] = Field(None, alias='friends')

    from_: typing.Optional[int] = Field(None, alias='from')

    outlier: typing.Optional[int] = Field(None, alias='outlier')

    guild: typing.Optional[bool] = Field(None, alias='guild')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
