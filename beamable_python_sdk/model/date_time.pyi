# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from beamable_python_sdk import schemas  # noqa: F401


class DateTime(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "dayOfYear",
            "equalNow",
            "year",
            "weekyear",
            "weekOfWeekyear",
            "secondOfMinute",
            "millisOfDay",
            "monthOfYear",
            "beforeNow",
            "dayOfWeek",
            "minuteOfDay",
            "dayOfMonth",
            "era",
            "yearOfCentury",
            "centuryOfEra",
            "hourOfDay",
            "secondOfDay",
            "millis",
            "yearOfEra",
            "minuteOfHour",
            "afterNow",
            "millisOfSecond",
        }
        
        class properties:
            dayOfYear = schemas.IntSchema
            minuteOfHour = schemas.IntSchema
            dayOfWeek = schemas.IntSchema
            hourOfDay = schemas.IntSchema
            dayOfMonth = schemas.IntSchema
            yearOfEra = schemas.IntSchema
            year = schemas.IntSchema
            secondOfDay = schemas.IntSchema
            yearOfCentury = schemas.IntSchema
            equalNow = schemas.BoolSchema
            afterNow = schemas.BoolSchema
            secondOfMinute = schemas.IntSchema
            monthOfYear = schemas.IntSchema
            millis = schemas.IntSchema
            beforeNow = schemas.BoolSchema
            centuryOfEra = schemas.IntSchema
            minuteOfDay = schemas.IntSchema
            era = schemas.IntSchema
            millisOfDay = schemas.IntSchema
            millisOfSecond = schemas.IntSchema
            weekOfWeekyear = schemas.IntSchema
            weekyear = schemas.IntSchema
        
            @staticmethod
            def chronology() -> typing.Type['Chronology']:
                return Chronology
        
            @staticmethod
            def zone() -> typing.Type['DateTimeZone']:
                return DateTimeZone
            __annotations__ = {
                "dayOfYear": dayOfYear,
                "minuteOfHour": minuteOfHour,
                "dayOfWeek": dayOfWeek,
                "hourOfDay": hourOfDay,
                "dayOfMonth": dayOfMonth,
                "yearOfEra": yearOfEra,
                "year": year,
                "secondOfDay": secondOfDay,
                "yearOfCentury": yearOfCentury,
                "equalNow": equalNow,
                "afterNow": afterNow,
                "secondOfMinute": secondOfMinute,
                "monthOfYear": monthOfYear,
                "millis": millis,
                "beforeNow": beforeNow,
                "centuryOfEra": centuryOfEra,
                "minuteOfDay": minuteOfDay,
                "era": era,
                "millisOfDay": millisOfDay,
                "millisOfSecond": millisOfSecond,
                "weekOfWeekyear": weekOfWeekyear,
                "weekyear": weekyear,
                "chronology": chronology,
                "zone": zone,
            }
    
    dayOfYear: MetaOapg.properties.dayOfYear
    equalNow: MetaOapg.properties.equalNow
    year: MetaOapg.properties.year
    weekyear: MetaOapg.properties.weekyear
    weekOfWeekyear: MetaOapg.properties.weekOfWeekyear
    secondOfMinute: MetaOapg.properties.secondOfMinute
    millisOfDay: MetaOapg.properties.millisOfDay
    monthOfYear: MetaOapg.properties.monthOfYear
    beforeNow: MetaOapg.properties.beforeNow
    dayOfWeek: MetaOapg.properties.dayOfWeek
    minuteOfDay: MetaOapg.properties.minuteOfDay
    dayOfMonth: MetaOapg.properties.dayOfMonth
    era: MetaOapg.properties.era
    yearOfCentury: MetaOapg.properties.yearOfCentury
    centuryOfEra: MetaOapg.properties.centuryOfEra
    hourOfDay: MetaOapg.properties.hourOfDay
    secondOfDay: MetaOapg.properties.secondOfDay
    millis: MetaOapg.properties.millis
    yearOfEra: MetaOapg.properties.yearOfEra
    minuteOfHour: MetaOapg.properties.minuteOfHour
    afterNow: MetaOapg.properties.afterNow
    millisOfSecond: MetaOapg.properties.millisOfSecond
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayOfYear"]) -> MetaOapg.properties.dayOfYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minuteOfHour"]) -> MetaOapg.properties.minuteOfHour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayOfWeek"]) -> MetaOapg.properties.dayOfWeek: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourOfDay"]) -> MetaOapg.properties.hourOfDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayOfMonth"]) -> MetaOapg.properties.dayOfMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yearOfEra"]) -> MetaOapg.properties.yearOfEra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondOfDay"]) -> MetaOapg.properties.secondOfDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yearOfCentury"]) -> MetaOapg.properties.yearOfCentury: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["equalNow"]) -> MetaOapg.properties.equalNow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["afterNow"]) -> MetaOapg.properties.afterNow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondOfMinute"]) -> MetaOapg.properties.secondOfMinute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthOfYear"]) -> MetaOapg.properties.monthOfYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["millis"]) -> MetaOapg.properties.millis: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beforeNow"]) -> MetaOapg.properties.beforeNow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["centuryOfEra"]) -> MetaOapg.properties.centuryOfEra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minuteOfDay"]) -> MetaOapg.properties.minuteOfDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["era"]) -> MetaOapg.properties.era: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["millisOfDay"]) -> MetaOapg.properties.millisOfDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["millisOfSecond"]) -> MetaOapg.properties.millisOfSecond: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekOfWeekyear"]) -> MetaOapg.properties.weekOfWeekyear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekyear"]) -> MetaOapg.properties.weekyear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chronology"]) -> 'Chronology': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zone"]) -> 'DateTimeZone': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dayOfYear", "minuteOfHour", "dayOfWeek", "hourOfDay", "dayOfMonth", "yearOfEra", "year", "secondOfDay", "yearOfCentury", "equalNow", "afterNow", "secondOfMinute", "monthOfYear", "millis", "beforeNow", "centuryOfEra", "minuteOfDay", "era", "millisOfDay", "millisOfSecond", "weekOfWeekyear", "weekyear", "chronology", "zone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayOfYear"]) -> MetaOapg.properties.dayOfYear: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minuteOfHour"]) -> MetaOapg.properties.minuteOfHour: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayOfWeek"]) -> MetaOapg.properties.dayOfWeek: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourOfDay"]) -> MetaOapg.properties.hourOfDay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayOfMonth"]) -> MetaOapg.properties.dayOfMonth: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yearOfEra"]) -> MetaOapg.properties.yearOfEra: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondOfDay"]) -> MetaOapg.properties.secondOfDay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yearOfCentury"]) -> MetaOapg.properties.yearOfCentury: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["equalNow"]) -> MetaOapg.properties.equalNow: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["afterNow"]) -> MetaOapg.properties.afterNow: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondOfMinute"]) -> MetaOapg.properties.secondOfMinute: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthOfYear"]) -> MetaOapg.properties.monthOfYear: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["millis"]) -> MetaOapg.properties.millis: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beforeNow"]) -> MetaOapg.properties.beforeNow: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["centuryOfEra"]) -> MetaOapg.properties.centuryOfEra: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minuteOfDay"]) -> MetaOapg.properties.minuteOfDay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["era"]) -> MetaOapg.properties.era: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["millisOfDay"]) -> MetaOapg.properties.millisOfDay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["millisOfSecond"]) -> MetaOapg.properties.millisOfSecond: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekOfWeekyear"]) -> MetaOapg.properties.weekOfWeekyear: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekyear"]) -> MetaOapg.properties.weekyear: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chronology"]) -> typing.Union['Chronology', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zone"]) -> typing.Union['DateTimeZone', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dayOfYear", "minuteOfHour", "dayOfWeek", "hourOfDay", "dayOfMonth", "yearOfEra", "year", "secondOfDay", "yearOfCentury", "equalNow", "afterNow", "secondOfMinute", "monthOfYear", "millis", "beforeNow", "centuryOfEra", "minuteOfDay", "era", "millisOfDay", "millisOfSecond", "weekOfWeekyear", "weekyear", "chronology", "zone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dayOfYear: typing.Union[MetaOapg.properties.dayOfYear, decimal.Decimal, int, ],
        equalNow: typing.Union[MetaOapg.properties.equalNow, bool, ],
        year: typing.Union[MetaOapg.properties.year, decimal.Decimal, int, ],
        weekyear: typing.Union[MetaOapg.properties.weekyear, decimal.Decimal, int, ],
        weekOfWeekyear: typing.Union[MetaOapg.properties.weekOfWeekyear, decimal.Decimal, int, ],
        secondOfMinute: typing.Union[MetaOapg.properties.secondOfMinute, decimal.Decimal, int, ],
        millisOfDay: typing.Union[MetaOapg.properties.millisOfDay, decimal.Decimal, int, ],
        monthOfYear: typing.Union[MetaOapg.properties.monthOfYear, decimal.Decimal, int, ],
        beforeNow: typing.Union[MetaOapg.properties.beforeNow, bool, ],
        dayOfWeek: typing.Union[MetaOapg.properties.dayOfWeek, decimal.Decimal, int, ],
        minuteOfDay: typing.Union[MetaOapg.properties.minuteOfDay, decimal.Decimal, int, ],
        dayOfMonth: typing.Union[MetaOapg.properties.dayOfMonth, decimal.Decimal, int, ],
        era: typing.Union[MetaOapg.properties.era, decimal.Decimal, int, ],
        yearOfCentury: typing.Union[MetaOapg.properties.yearOfCentury, decimal.Decimal, int, ],
        centuryOfEra: typing.Union[MetaOapg.properties.centuryOfEra, decimal.Decimal, int, ],
        hourOfDay: typing.Union[MetaOapg.properties.hourOfDay, decimal.Decimal, int, ],
        secondOfDay: typing.Union[MetaOapg.properties.secondOfDay, decimal.Decimal, int, ],
        millis: typing.Union[MetaOapg.properties.millis, decimal.Decimal, int, ],
        yearOfEra: typing.Union[MetaOapg.properties.yearOfEra, decimal.Decimal, int, ],
        minuteOfHour: typing.Union[MetaOapg.properties.minuteOfHour, decimal.Decimal, int, ],
        afterNow: typing.Union[MetaOapg.properties.afterNow, bool, ],
        millisOfSecond: typing.Union[MetaOapg.properties.millisOfSecond, decimal.Decimal, int, ],
        chronology: typing.Union['Chronology', schemas.Unset] = schemas.unset,
        zone: typing.Union['DateTimeZone', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DateTime':
        return super().__new__(
            cls,
            *args,
            dayOfYear=dayOfYear,
            equalNow=equalNow,
            year=year,
            weekyear=weekyear,
            weekOfWeekyear=weekOfWeekyear,
            secondOfMinute=secondOfMinute,
            millisOfDay=millisOfDay,
            monthOfYear=monthOfYear,
            beforeNow=beforeNow,
            dayOfWeek=dayOfWeek,
            minuteOfDay=minuteOfDay,
            dayOfMonth=dayOfMonth,
            era=era,
            yearOfCentury=yearOfCentury,
            centuryOfEra=centuryOfEra,
            hourOfDay=hourOfDay,
            secondOfDay=secondOfDay,
            millis=millis,
            yearOfEra=yearOfEra,
            minuteOfHour=minuteOfHour,
            afterNow=afterNow,
            millisOfSecond=millisOfSecond,
            chronology=chronology,
            zone=zone,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.chronology import Chronology
from beamable_python_sdk.model.date_time_zone import DateTimeZone
