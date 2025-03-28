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


class PlayerStoreView(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            
            
            class listings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PlayerListingView']:
                        return PlayerListingView
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PlayerListingView'], typing.List['PlayerListingView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'listings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PlayerListingView':
                    return super().__getitem__(i)
            symbol = schemas.StrSchema
            nextDeltaSeconds = schemas.IntSchema
            secondsRemain = schemas.IntSchema
            __annotations__ = {
                "title": title,
                "listings": listings,
                "symbol": symbol,
                "nextDeltaSeconds": nextDeltaSeconds,
                "secondsRemain": secondsRemain,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listings"]) -> MetaOapg.properties.listings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextDeltaSeconds"]) -> MetaOapg.properties.nextDeltaSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondsRemain"]) -> MetaOapg.properties.secondsRemain: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "listings", "symbol", "nextDeltaSeconds", "secondsRemain", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listings"]) -> typing.Union[MetaOapg.properties.listings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> typing.Union[MetaOapg.properties.symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextDeltaSeconds"]) -> typing.Union[MetaOapg.properties.nextDeltaSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondsRemain"]) -> typing.Union[MetaOapg.properties.secondsRemain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "listings", "symbol", "nextDeltaSeconds", "secondsRemain", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        listings: typing.Union[MetaOapg.properties.listings, list, tuple, schemas.Unset] = schemas.unset,
        symbol: typing.Union[MetaOapg.properties.symbol, str, schemas.Unset] = schemas.unset,
        nextDeltaSeconds: typing.Union[MetaOapg.properties.nextDeltaSeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        secondsRemain: typing.Union[MetaOapg.properties.secondsRemain, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PlayerStoreView':
        return super().__new__(
            cls,
            *args,
            title=title,
            listings=listings,
            symbol=symbol,
            nextDeltaSeconds=nextDeltaSeconds,
            secondsRemain=secondsRemain,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.player_listing_view import PlayerListingView
