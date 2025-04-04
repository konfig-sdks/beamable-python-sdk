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


class EventPhaseRuntime(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "startTime",
            "endTime",
        }
        
        class properties:
            startTime = schemas.IntSchema
            endTime = schemas.IntSchema
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
                "startTime": startTime,
                "endTime": endTime,
                "name": name,
                "rules": rules,
            }
    
    startTime: MetaOapg.properties.startTime
    endTime: MetaOapg.properties.endTime
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endTime"]) -> MetaOapg.properties.endTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rules"]) -> MetaOapg.properties.rules: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["startTime", "endTime", "name", "rules", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endTime"]) -> MetaOapg.properties.endTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rules"]) -> typing.Union[MetaOapg.properties.rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["startTime", "endTime", "name", "rules", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        startTime: typing.Union[MetaOapg.properties.startTime, decimal.Decimal, int, ],
        endTime: typing.Union[MetaOapg.properties.endTime, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        rules: typing.Union[MetaOapg.properties.rules, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventPhaseRuntime':
        return super().__new__(
            cls,
            *args,
            startTime=startTime,
            endTime=endTime,
            name=name,
            rules=rules,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.event_rule import EventRule
