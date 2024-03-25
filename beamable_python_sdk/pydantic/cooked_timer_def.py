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


class CookedTimerDef(BaseModel):
    secs_till_fire: int = Field(alias='secsTillFire')

    next_fire: int = Field(alias='nextFire')

    secs_in_period: int = Field(alias='secsInPeriod')

    name: typing.Optional[str] = Field(None, alias='name')

    cronish: typing.Optional[str] = Field(None, alias='cronish')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
