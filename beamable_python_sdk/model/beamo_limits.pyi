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


class BeamoLimits(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "maxRunningContainersPerService",
            "maxContainerSize",
        }
        
        class properties:
            maxContainerSize = schemas.StrSchema
            maxRunningContainersPerService = schemas.Int32Schema
            __annotations__ = {
                "maxContainerSize": maxContainerSize,
                "maxRunningContainersPerService": maxRunningContainersPerService,
            }
    
    maxRunningContainersPerService: MetaOapg.properties.maxRunningContainersPerService
    maxContainerSize: MetaOapg.properties.maxContainerSize
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxContainerSize"]) -> MetaOapg.properties.maxContainerSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxRunningContainersPerService"]) -> MetaOapg.properties.maxRunningContainersPerService: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxContainerSize", "maxRunningContainersPerService", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxContainerSize"]) -> MetaOapg.properties.maxContainerSize: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxRunningContainersPerService"]) -> MetaOapg.properties.maxRunningContainersPerService: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxContainerSize", "maxRunningContainersPerService", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        maxRunningContainersPerService: typing.Union[MetaOapg.properties.maxRunningContainersPerService, decimal.Decimal, int, ],
        maxContainerSize: typing.Union[MetaOapg.properties.maxContainerSize, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BeamoLimits':
        return super().__new__(
            cls,
            *args,
            maxRunningContainersPerService=maxRunningContainersPerService,
            maxContainerSize=maxContainerSize,
            _configuration=_configuration,
            **kwargs,
        )
