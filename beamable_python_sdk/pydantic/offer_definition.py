# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from beamable_python_sdk.pydantic.commerce_loot_roll import CommerceLootRoll
from beamable_python_sdk.pydantic.currency_change import CurrencyChange
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest
from beamable_python_sdk.pydantic.offer_definition_descriptions import OfferDefinitionDescriptions
from beamable_python_sdk.pydantic.offer_definition_images import OfferDefinitionImages
from beamable_python_sdk.pydantic.offer_definition_obtain import OfferDefinitionObtain
from beamable_python_sdk.pydantic.offer_definition_titles import OfferDefinitionTitles

class OfferDefinition(BaseModel):
    titles: typing.Optional[OfferDefinitionTitles] = Field(None, alias='titles')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    obtain_items: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='obtainItems')

    loot_roll: typing.Optional[CommerceLootRoll] = Field(None, alias='lootRoll')

    obtain_currency: typing.Optional[typing.List[CurrencyChange]] = Field(None, alias='obtainCurrency')

    metadata: typing.Optional[str] = Field(None, alias='metadata')

    images: typing.Optional[OfferDefinitionImages] = Field(None, alias='images')

    descriptions: typing.Optional[OfferDefinitionDescriptions] = Field(None, alias='descriptions')

    obtain: typing.Optional[OfferDefinitionObtain] = Field(None, alias='obtain')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
