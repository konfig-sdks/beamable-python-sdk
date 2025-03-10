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


class Cohort(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "assigned",
        }
        
        class properties:
            assigned = schemas.IntSchema
            name = schemas.StrSchema
            
            
            class customRule(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomCohortRule']:
                        return CustomCohortRule
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomCohortRule'], typing.List['CustomCohortRule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customRule':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomCohortRule':
                    return super().__getitem__(i)
            populationCap = schemas.IntSchema
            pct = schemas.IntSchema
            
            
            class cloudData(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CloudStorage']:
                        return CloudStorage
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CloudStorage'], typing.List['CloudStorage']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cloudData':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CloudStorage':
                    return super().__getitem__(i)
            __annotations__ = {
                "assigned": assigned,
                "name": name,
                "customRule": customRule,
                "populationCap": populationCap,
                "pct": pct,
                "cloudData": cloudData,
            }
    
    assigned: MetaOapg.properties.assigned
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assigned"]) -> MetaOapg.properties.assigned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customRule"]) -> MetaOapg.properties.customRule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["populationCap"]) -> MetaOapg.properties.populationCap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pct"]) -> MetaOapg.properties.pct: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloudData"]) -> MetaOapg.properties.cloudData: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assigned", "name", "customRule", "populationCap", "pct", "cloudData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assigned"]) -> MetaOapg.properties.assigned: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customRule"]) -> typing.Union[MetaOapg.properties.customRule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["populationCap"]) -> typing.Union[MetaOapg.properties.populationCap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pct"]) -> typing.Union[MetaOapg.properties.pct, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloudData"]) -> typing.Union[MetaOapg.properties.cloudData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assigned", "name", "customRule", "populationCap", "pct", "cloudData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        assigned: typing.Union[MetaOapg.properties.assigned, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        customRule: typing.Union[MetaOapg.properties.customRule, list, tuple, schemas.Unset] = schemas.unset,
        populationCap: typing.Union[MetaOapg.properties.populationCap, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pct: typing.Union[MetaOapg.properties.pct, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cloudData: typing.Union[MetaOapg.properties.cloudData, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Cohort':
        return super().__new__(
            cls,
            *args,
            assigned=assigned,
            name=name,
            customRule=customRule,
            populationCap=populationCap,
            pct=pct,
            cloudData=cloudData,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.cloud_storage import CloudStorage
from beamable_python_sdk.model.custom_cohort_rule import CustomCohortRule
