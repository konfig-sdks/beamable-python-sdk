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

from beamable_python_sdk.pydantic.chronology import Chronology
from beamable_python_sdk.pydantic.date_time_zone import DateTimeZone

class DateTime(BaseModel):
    day_of_year: int = Field(alias='dayOfYear')

    minute_of_hour: int = Field(alias='minuteOfHour')

    day_of_week: int = Field(alias='dayOfWeek')

    hour_of_day: int = Field(alias='hourOfDay')

    day_of_month: int = Field(alias='dayOfMonth')

    year_of_era: int = Field(alias='yearOfEra')

    year: int = Field(alias='year')

    second_of_day: int = Field(alias='secondOfDay')

    year_of_century: int = Field(alias='yearOfCentury')

    equal_now: bool = Field(alias='equalNow')

    after_now: bool = Field(alias='afterNow')

    second_of_minute: int = Field(alias='secondOfMinute')

    month_of_year: int = Field(alias='monthOfYear')

    millis: int = Field(alias='millis')

    before_now: bool = Field(alias='beforeNow')

    century_of_era: int = Field(alias='centuryOfEra')

    minute_of_day: int = Field(alias='minuteOfDay')

    era: int = Field(alias='era')

    millis_of_day: int = Field(alias='millisOfDay')

    millis_of_second: int = Field(alias='millisOfSecond')

    week_of_weekyear: int = Field(alias='weekOfWeekyear')

    weekyear: int = Field(alias='weekyear')

    chronology: typing.Optional[Chronology] = Field(None, alias='chronology')

    zone: typing.Optional[DateTimeZone] = Field(None, alias='zone')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
