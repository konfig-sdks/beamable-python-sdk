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


class ServicePlan(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "dataDomain",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def dataDomain() -> typing.Type['DataDomain']:
                return DataDomain
            minCustomerStatusSaved = schemas.StrSchema
        
            @staticmethod
            def limits() -> typing.Type['ServiceLimits']:
                return ServiceLimits
            created = schemas.Int64Schema
            __annotations__ = {
                "name": name,
                "dataDomain": dataDomain,
                "minCustomerStatusSaved": minCustomerStatusSaved,
                "limits": limits,
                "created": created,
            }
    
    dataDomain: 'DataDomain'
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataDomain"]) -> 'DataDomain': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minCustomerStatusSaved"]) -> MetaOapg.properties.minCustomerStatusSaved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limits"]) -> 'ServiceLimits': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "dataDomain", "minCustomerStatusSaved", "limits", "created", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataDomain"]) -> 'DataDomain': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minCustomerStatusSaved"]) -> typing.Union[MetaOapg.properties.minCustomerStatusSaved, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limits"]) -> typing.Union['ServiceLimits', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "dataDomain", "minCustomerStatusSaved", "limits", "created", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dataDomain: 'DataDomain',
        name: typing.Union[MetaOapg.properties.name, str, ],
        minCustomerStatusSaved: typing.Union[MetaOapg.properties.minCustomerStatusSaved, str, schemas.Unset] = schemas.unset,
        limits: typing.Union['ServiceLimits', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServicePlan':
        return super().__new__(
            cls,
            *args,
            dataDomain=dataDomain,
            name=name,
            minCustomerStatusSaved=minCustomerStatusSaved,
            limits=limits,
            created=created,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.data_domain import DataDomain
from beamable_python_sdk.model.service_limits import ServiceLimits
