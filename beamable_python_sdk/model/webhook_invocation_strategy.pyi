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


class WebhookInvocationStrategy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            invocationType = schemas.StrSchema
            retryType = schemas.StrSchema
            __annotations__ = {
                "invocationType": invocationType,
                "retryType": retryType,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invocationType"]) -> MetaOapg.properties.invocationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retryType"]) -> MetaOapg.properties.retryType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["invocationType", "retryType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invocationType"]) -> typing.Union[MetaOapg.properties.invocationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retryType"]) -> typing.Union[MetaOapg.properties.retryType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["invocationType", "retryType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        invocationType: typing.Union[MetaOapg.properties.invocationType, str, schemas.Unset] = schemas.unset,
        retryType: typing.Union[MetaOapg.properties.retryType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookInvocationStrategy':
        return super().__new__(
            cls,
            *args,
            invocationType=invocationType,
            retryType=retryType,
            _configuration=_configuration,
            **kwargs,
        )
