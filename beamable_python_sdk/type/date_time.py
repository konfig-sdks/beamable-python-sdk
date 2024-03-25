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

from beamable_python_sdk.type.chronology import Chronology
from beamable_python_sdk.type.date_time_zone import DateTimeZone

class RequiredDateTime(TypedDict):
    dayOfYear: int

    minuteOfHour: int

    dayOfWeek: int

    hourOfDay: int

    dayOfMonth: int

    yearOfEra: int

    year: int

    secondOfDay: int

    yearOfCentury: int

    equalNow: bool

    afterNow: bool

    secondOfMinute: int

    monthOfYear: int

    millis: int

    beforeNow: bool

    centuryOfEra: int

    minuteOfDay: int

    era: int

    millisOfDay: int

    millisOfSecond: int

    weekOfWeekyear: int

    weekyear: int

class OptionalDateTime(TypedDict, total=False):
    chronology: Chronology

    zone: DateTimeZone

class DateTime(RequiredDateTime, OptionalDateTime):
    pass
