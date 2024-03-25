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


class PromoteRealmResponseOld(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "promotions",
            "sourcePid",
        }
        
        class properties:
            sourcePid = schemas.StrSchema
            
            
            class promotions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RealmPromotion']:
                        return RealmPromotion
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['RealmPromotion'], typing.List['RealmPromotion']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'promotions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RealmPromotion':
                    return super().__getitem__(i)
            __annotations__ = {
                "sourcePid": sourcePid,
                "promotions": promotions,
            }
    
    promotions: MetaOapg.properties.promotions
    sourcePid: MetaOapg.properties.sourcePid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourcePid"]) -> MetaOapg.properties.sourcePid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["promotions"]) -> MetaOapg.properties.promotions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sourcePid", "promotions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourcePid"]) -> MetaOapg.properties.sourcePid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["promotions"]) -> MetaOapg.properties.promotions: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sourcePid", "promotions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        promotions: typing.Union[MetaOapg.properties.promotions, list, tuple, ],
        sourcePid: typing.Union[MetaOapg.properties.sourcePid, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PromoteRealmResponseOld':
        return super().__new__(
            cls,
            *args,
            promotions=promotions,
            sourcePid=sourcePid,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.realm_promotion import RealmPromotion
