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


class PromoteRealmResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sourcePid",
            "scopes",
        }
        
        class properties:
            sourcePid = schemas.StrSchema
            
            
            class scopes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PromotionScope']:
                        return PromotionScope
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PromotionScope'], typing.List['PromotionScope']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scopes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PromotionScope':
                    return super().__getitem__(i)
            __annotations__ = {
                "sourcePid": sourcePid,
                "scopes": scopes,
            }
    
    sourcePid: MetaOapg.properties.sourcePid
    scopes: MetaOapg.properties.scopes
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourcePid"]) -> MetaOapg.properties.sourcePid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sourcePid", "scopes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourcePid"]) -> MetaOapg.properties.sourcePid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sourcePid", "scopes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sourcePid: typing.Union[MetaOapg.properties.sourcePid, str, ],
        scopes: typing.Union[MetaOapg.properties.scopes, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PromoteRealmResponse':
        return super().__new__(
            cls,
            *args,
            sourcePid=sourcePid,
            scopes=scopes,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.promotion_scope import PromotionScope
