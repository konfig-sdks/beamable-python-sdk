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


class OfferDefinition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def titles() -> typing.Type['OfferDefinitionTitles']:
                return OfferDefinitionTitles
            symbol = schemas.StrSchema
            
            
            class obtainItems(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ItemCreateRequest']:
                        return ItemCreateRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ItemCreateRequest'], typing.List['ItemCreateRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'obtainItems':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ItemCreateRequest':
                    return super().__getitem__(i)
        
            @staticmethod
            def lootRoll() -> typing.Type['CommerceLootRoll']:
                return CommerceLootRoll
            
            
            class obtainCurrency(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CurrencyChange']:
                        return CurrencyChange
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CurrencyChange'], typing.List['CurrencyChange']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'obtainCurrency':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CurrencyChange':
                    return super().__getitem__(i)
            metadata = schemas.StrSchema
        
            @staticmethod
            def images() -> typing.Type['OfferDefinitionImages']:
                return OfferDefinitionImages
        
            @staticmethod
            def descriptions() -> typing.Type['OfferDefinitionDescriptions']:
                return OfferDefinitionDescriptions
        
            @staticmethod
            def obtain() -> typing.Type['OfferDefinitionObtain']:
                return OfferDefinitionObtain
            __annotations__ = {
                "titles": titles,
                "symbol": symbol,
                "obtainItems": obtainItems,
                "lootRoll": lootRoll,
                "obtainCurrency": obtainCurrency,
                "metadata": metadata,
                "images": images,
                "descriptions": descriptions,
                "obtain": obtain,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["titles"]) -> 'OfferDefinitionTitles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["obtainItems"]) -> MetaOapg.properties.obtainItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lootRoll"]) -> 'CommerceLootRoll': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["obtainCurrency"]) -> MetaOapg.properties.obtainCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["images"]) -> 'OfferDefinitionImages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["descriptions"]) -> 'OfferDefinitionDescriptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["obtain"]) -> 'OfferDefinitionObtain': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["titles", "symbol", "obtainItems", "lootRoll", "obtainCurrency", "metadata", "images", "descriptions", "obtain", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["titles"]) -> typing.Union['OfferDefinitionTitles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> typing.Union[MetaOapg.properties.symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["obtainItems"]) -> typing.Union[MetaOapg.properties.obtainItems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lootRoll"]) -> typing.Union['CommerceLootRoll', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["obtainCurrency"]) -> typing.Union[MetaOapg.properties.obtainCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["images"]) -> typing.Union['OfferDefinitionImages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["descriptions"]) -> typing.Union['OfferDefinitionDescriptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["obtain"]) -> typing.Union['OfferDefinitionObtain', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["titles", "symbol", "obtainItems", "lootRoll", "obtainCurrency", "metadata", "images", "descriptions", "obtain", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        titles: typing.Union['OfferDefinitionTitles', schemas.Unset] = schemas.unset,
        symbol: typing.Union[MetaOapg.properties.symbol, str, schemas.Unset] = schemas.unset,
        obtainItems: typing.Union[MetaOapg.properties.obtainItems, list, tuple, schemas.Unset] = schemas.unset,
        lootRoll: typing.Union['CommerceLootRoll', schemas.Unset] = schemas.unset,
        obtainCurrency: typing.Union[MetaOapg.properties.obtainCurrency, list, tuple, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, str, schemas.Unset] = schemas.unset,
        images: typing.Union['OfferDefinitionImages', schemas.Unset] = schemas.unset,
        descriptions: typing.Union['OfferDefinitionDescriptions', schemas.Unset] = schemas.unset,
        obtain: typing.Union['OfferDefinitionObtain', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OfferDefinition':
        return super().__new__(
            cls,
            *args,
            titles=titles,
            symbol=symbol,
            obtainItems=obtainItems,
            lootRoll=lootRoll,
            obtainCurrency=obtainCurrency,
            metadata=metadata,
            images=images,
            descriptions=descriptions,
            obtain=obtain,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.commerce_loot_roll import CommerceLootRoll
from beamable_python_sdk.model.currency_change import CurrencyChange
from beamable_python_sdk.model.item_create_request import ItemCreateRequest
from beamable_python_sdk.model.offer_definition_descriptions import OfferDefinitionDescriptions
from beamable_python_sdk.model.offer_definition_images import OfferDefinitionImages
from beamable_python_sdk.model.offer_definition_obtain import OfferDefinitionObtain
from beamable_python_sdk.model.offer_definition_titles import OfferDefinitionTitles
