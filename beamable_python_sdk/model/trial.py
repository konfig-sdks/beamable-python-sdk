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


class Trial(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "active",
            "assigned",
        }
        
        class properties:
            assigned = schemas.IntSchema
            active = schemas.BoolSchema
            name = schemas.StrSchema
            activated = schemas.IntSchema
            
            
            class cohorts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Cohort']:
                        return Cohort
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Cohort'], typing.List['Cohort']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cohorts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Cohort':
                    return super().__getitem__(i)
            ctype = schemas.StrSchema
            scheduleStart = schemas.IntSchema
            strategy = schemas.StrSchema
            ttype = schemas.StrSchema
            created = schemas.IntSchema
            __annotations__ = {
                "assigned": assigned,
                "active": active,
                "name": name,
                "activated": activated,
                "cohorts": cohorts,
                "ctype": ctype,
                "scheduleStart": scheduleStart,
                "strategy": strategy,
                "ttype": ttype,
                "created": created,
            }
    
    active: MetaOapg.properties.active
    assigned: MetaOapg.properties.assigned
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assigned"]) -> MetaOapg.properties.assigned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activated"]) -> MetaOapg.properties.activated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cohorts"]) -> MetaOapg.properties.cohorts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ctype"]) -> MetaOapg.properties.ctype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduleStart"]) -> MetaOapg.properties.scheduleStart: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strategy"]) -> MetaOapg.properties.strategy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttype"]) -> MetaOapg.properties.ttype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assigned", "active", "name", "activated", "cohorts", "ctype", "scheduleStart", "strategy", "ttype", "created", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assigned"]) -> MetaOapg.properties.assigned: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activated"]) -> typing.Union[MetaOapg.properties.activated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cohorts"]) -> typing.Union[MetaOapg.properties.cohorts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ctype"]) -> typing.Union[MetaOapg.properties.ctype, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduleStart"]) -> typing.Union[MetaOapg.properties.scheduleStart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strategy"]) -> typing.Union[MetaOapg.properties.strategy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttype"]) -> typing.Union[MetaOapg.properties.ttype, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assigned", "active", "name", "activated", "cohorts", "ctype", "scheduleStart", "strategy", "ttype", "created", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        active: typing.Union[MetaOapg.properties.active, bool, ],
        assigned: typing.Union[MetaOapg.properties.assigned, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        activated: typing.Union[MetaOapg.properties.activated, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cohorts: typing.Union[MetaOapg.properties.cohorts, list, tuple, schemas.Unset] = schemas.unset,
        ctype: typing.Union[MetaOapg.properties.ctype, str, schemas.Unset] = schemas.unset,
        scheduleStart: typing.Union[MetaOapg.properties.scheduleStart, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        strategy: typing.Union[MetaOapg.properties.strategy, str, schemas.Unset] = schemas.unset,
        ttype: typing.Union[MetaOapg.properties.ttype, str, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Trial':
        return super().__new__(
            cls,
            *args,
            active=active,
            assigned=assigned,
            name=name,
            activated=activated,
            cohorts=cohorts,
            ctype=ctype,
            scheduleStart=scheduleStart,
            strategy=strategy,
            ttype=ttype,
            created=created,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.cohort import Cohort
