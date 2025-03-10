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


class PlayerListingView(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "queryAfterPurchase",
            "active",
            "secondsActive",
        }
        
        class properties:
            secondsActive = schemas.IntSchema
            queryAfterPurchase = schemas.BoolSchema
            active = schemas.BoolSchema
            
            
            class clientDataList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ClientDataEntry']:
                        return ClientDataEntry
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ClientDataEntry'], typing.List['ClientDataEntry']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clientDataList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ClientDataEntry':
                    return super().__getitem__(i)
            symbol = schemas.StrSchema
        
            @staticmethod
            def clientData() -> typing.Type['PlayerListingViewClientData']:
                return PlayerListingViewClientData
            cooldown = schemas.IntSchema
        
            @staticmethod
            def offer() -> typing.Type['PlayerOfferView']:
                return PlayerOfferView
            purchasesRemain = schemas.IntSchema
            secondsRemain = schemas.IntSchema
            __annotations__ = {
                "secondsActive": secondsActive,
                "queryAfterPurchase": queryAfterPurchase,
                "active": active,
                "clientDataList": clientDataList,
                "symbol": symbol,
                "clientData": clientData,
                "cooldown": cooldown,
                "offer": offer,
                "purchasesRemain": purchasesRemain,
                "secondsRemain": secondsRemain,
            }
    
    queryAfterPurchase: MetaOapg.properties.queryAfterPurchase
    active: MetaOapg.properties.active
    secondsActive: MetaOapg.properties.secondsActive
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondsActive"]) -> MetaOapg.properties.secondsActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["queryAfterPurchase"]) -> MetaOapg.properties.queryAfterPurchase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientDataList"]) -> MetaOapg.properties.clientDataList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientData"]) -> 'PlayerListingViewClientData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cooldown"]) -> MetaOapg.properties.cooldown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offer"]) -> 'PlayerOfferView': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchasesRemain"]) -> MetaOapg.properties.purchasesRemain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondsRemain"]) -> MetaOapg.properties.secondsRemain: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["secondsActive", "queryAfterPurchase", "active", "clientDataList", "symbol", "clientData", "cooldown", "offer", "purchasesRemain", "secondsRemain", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondsActive"]) -> MetaOapg.properties.secondsActive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["queryAfterPurchase"]) -> MetaOapg.properties.queryAfterPurchase: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientDataList"]) -> typing.Union[MetaOapg.properties.clientDataList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> typing.Union[MetaOapg.properties.symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientData"]) -> typing.Union['PlayerListingViewClientData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cooldown"]) -> typing.Union[MetaOapg.properties.cooldown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offer"]) -> typing.Union['PlayerOfferView', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchasesRemain"]) -> typing.Union[MetaOapg.properties.purchasesRemain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondsRemain"]) -> typing.Union[MetaOapg.properties.secondsRemain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["secondsActive", "queryAfterPurchase", "active", "clientDataList", "symbol", "clientData", "cooldown", "offer", "purchasesRemain", "secondsRemain", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        queryAfterPurchase: typing.Union[MetaOapg.properties.queryAfterPurchase, bool, ],
        active: typing.Union[MetaOapg.properties.active, bool, ],
        secondsActive: typing.Union[MetaOapg.properties.secondsActive, decimal.Decimal, int, ],
        clientDataList: typing.Union[MetaOapg.properties.clientDataList, list, tuple, schemas.Unset] = schemas.unset,
        symbol: typing.Union[MetaOapg.properties.symbol, str, schemas.Unset] = schemas.unset,
        clientData: typing.Union['PlayerListingViewClientData', schemas.Unset] = schemas.unset,
        cooldown: typing.Union[MetaOapg.properties.cooldown, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        offer: typing.Union['PlayerOfferView', schemas.Unset] = schemas.unset,
        purchasesRemain: typing.Union[MetaOapg.properties.purchasesRemain, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        secondsRemain: typing.Union[MetaOapg.properties.secondsRemain, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PlayerListingView':
        return super().__new__(
            cls,
            *args,
            queryAfterPurchase=queryAfterPurchase,
            active=active,
            secondsActive=secondsActive,
            clientDataList=clientDataList,
            symbol=symbol,
            clientData=clientData,
            cooldown=cooldown,
            offer=offer,
            purchasesRemain=purchasesRemain,
            secondsRemain=secondsRemain,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.client_data_entry import ClientDataEntry
from beamable_python_sdk.model.player_listing_view_client_data import PlayerListingViewClientData
from beamable_python_sdk.model.player_offer_view import PlayerOfferView
