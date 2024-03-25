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

from beamable_python_sdk.pydantic.reward_calendar_day import RewardCalendarDay

class CalendarView(BaseModel):
    next_index: int = Field(alias='nextIndex')

    next_claim_seconds: int = Field(alias='nextClaimSeconds')

    remaining_seconds: int = Field(alias='remainingSeconds')

    id: typing.Optional[str] = Field(None, alias='id')

    days: typing.Optional[typing.List[RewardCalendarDay]] = Field(None, alias='days')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
