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


class EventPhase(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "duration_minutes",
            "durationSeconds",
            "durationMillis",
        }
        
        class properties:
            duration_minutes = schemas.IntSchema
            durationMillis = schemas.IntSchema
            durationSeconds = schemas.IntSchema
            name = schemas.StrSchema
            
            
            class rules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EventRule']:
                        return EventRule
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EventRule'], typing.List['EventRule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rules':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EventRule':
                    return super().__getitem__(i)
            __annotations__ = {
                "duration_minutes": duration_minutes,
                "durationMillis": durationMillis,
                "durationSeconds": durationSeconds,
                "name": name,
                "rules": rules,
            }
    
    duration_minutes: MetaOapg.properties.duration_minutes
    durationSeconds: MetaOapg.properties.durationSeconds
    durationMillis: MetaOapg.properties.durationMillis
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_minutes"]) -> MetaOapg.properties.duration_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["durationMillis"]) -> MetaOapg.properties.durationMillis: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["durationSeconds"]) -> MetaOapg.properties.durationSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rules"]) -> MetaOapg.properties.rules: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["duration_minutes", "durationMillis", "durationSeconds", "name", "rules", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_minutes"]) -> MetaOapg.properties.duration_minutes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["durationMillis"]) -> MetaOapg.properties.durationMillis: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["durationSeconds"]) -> MetaOapg.properties.durationSeconds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rules"]) -> typing.Union[MetaOapg.properties.rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["duration_minutes", "durationMillis", "durationSeconds", "name", "rules", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        duration_minutes: typing.Union[MetaOapg.properties.duration_minutes, decimal.Decimal, int, ],
        durationSeconds: typing.Union[MetaOapg.properties.durationSeconds, decimal.Decimal, int, ],
        durationMillis: typing.Union[MetaOapg.properties.durationMillis, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        rules: typing.Union[MetaOapg.properties.rules, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventPhase':
        return super().__new__(
            cls,
            *args,
            duration_minutes=duration_minutes,
            durationSeconds=durationSeconds,
            durationMillis=durationMillis,
            name=name,
            rules=rules,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.event_rule import EventRule
