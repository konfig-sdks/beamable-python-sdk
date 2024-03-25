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

from beamable_python_sdk.pydantic.era import Era
from beamable_python_sdk.pydantic.iso_chronology import IsoChronology

class LocalDate(BaseModel):
    day_of_year: int = Field(alias='dayOfYear')

    leap_year: bool = Field(alias='leapYear')

    month_value: int = Field(alias='monthValue')

    day_of_month: int = Field(alias='dayOfMonth')

    year: int = Field(alias='year')

    chronology: typing.Optional[IsoChronology] = Field(None, alias='chronology')

    day_of_week: typing.Optional[Literal["SATURDAY", "MONDAY", "THURSDAY", "TUESDAY", "FRIDAY", "WEDNESDAY", "SUNDAY"]] = Field(None, alias='dayOfWeek')

    era: typing.Optional[Era] = Field(None, alias='era')

    month: typing.Optional[Literal["DECEMBER", "APRIL", "JULY", "SEPTEMBER", "JUNE", "FEBRUARY", "OCTOBER", "AUGUST", "NOVEMBER", "MARCH", "MAY", "JANUARY"]] = Field(None, alias='month')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
