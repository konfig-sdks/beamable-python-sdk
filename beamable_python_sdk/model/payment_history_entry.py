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


class PaymentHistoryEntry(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "MAX_FIELD_SIZE",
        }
        
        class properties:
            MAX_FIELD_SIZE = schemas.IntSchema
            change = schemas.StrSchema
            data = schemas.StrSchema
            timestamp = schemas.StrSchema
            __annotations__ = {
                "MAX_FIELD_SIZE": MAX_FIELD_SIZE,
                "change": change,
                "data": data,
                "timestamp": timestamp,
            }
    
    MAX_FIELD_SIZE: MetaOapg.properties.MAX_FIELD_SIZE
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MAX_FIELD_SIZE"]) -> MetaOapg.properties.MAX_FIELD_SIZE: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["change"]) -> MetaOapg.properties.change: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["MAX_FIELD_SIZE", "change", "data", "timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MAX_FIELD_SIZE"]) -> MetaOapg.properties.MAX_FIELD_SIZE: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["change"]) -> typing.Union[MetaOapg.properties.change, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["MAX_FIELD_SIZE", "change", "data", "timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        MAX_FIELD_SIZE: typing.Union[MetaOapg.properties.MAX_FIELD_SIZE, decimal.Decimal, int, ],
        change: typing.Union[MetaOapg.properties.change, str, schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, str, schemas.Unset] = schemas.unset,
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentHistoryEntry':
        return super().__new__(
            cls,
            *args,
            MAX_FIELD_SIZE=MAX_FIELD_SIZE,
            change=change,
            data=data,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )
