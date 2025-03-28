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


class LeaderboardGetMatchRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "windowSize",
            "poolSize",
            "windows",
        }
        
        class properties:
            poolSize = schemas.IntSchema
            windows = schemas.IntSchema
            windowSize = schemas.IntSchema
            __annotations__ = {
                "poolSize": poolSize,
                "windows": windows,
                "windowSize": windowSize,
            }
    
    windowSize: MetaOapg.properties.windowSize
    poolSize: MetaOapg.properties.poolSize
    windows: MetaOapg.properties.windows
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["poolSize"]) -> MetaOapg.properties.poolSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["windows"]) -> MetaOapg.properties.windows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["windowSize"]) -> MetaOapg.properties.windowSize: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["poolSize", "windows", "windowSize", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["poolSize"]) -> MetaOapg.properties.poolSize: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["windows"]) -> MetaOapg.properties.windows: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["windowSize"]) -> MetaOapg.properties.windowSize: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["poolSize", "windows", "windowSize", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        windowSize: typing.Union[MetaOapg.properties.windowSize, decimal.Decimal, int, ],
        poolSize: typing.Union[MetaOapg.properties.poolSize, decimal.Decimal, int, ],
        windows: typing.Union[MetaOapg.properties.windows, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LeaderboardGetMatchRequest':
        return super().__new__(
            cls,
            *args,
            windowSize=windowSize,
            poolSize=poolSize,
            windows=windows,
            _configuration=_configuration,
            **kwargs,
        )
