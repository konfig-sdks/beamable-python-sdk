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

from beamable_python_sdk.type.commerce_loot_roll import CommerceLootRoll
from beamable_python_sdk.type.currency_change import CurrencyChange
from beamable_python_sdk.type.item_create_request import ItemCreateRequest
from beamable_python_sdk.type.offer_definition_descriptions import OfferDefinitionDescriptions
from beamable_python_sdk.type.offer_definition_images import OfferDefinitionImages
from beamable_python_sdk.type.offer_definition_obtain import OfferDefinitionObtain
from beamable_python_sdk.type.offer_definition_titles import OfferDefinitionTitles

class RequiredOfferDefinition(TypedDict):
    pass

class OptionalOfferDefinition(TypedDict, total=False):
    titles: OfferDefinitionTitles

    symbol: str

    obtainItems: typing.List[ItemCreateRequest]

    lootRoll: CommerceLootRoll

    obtainCurrency: typing.List[CurrencyChange]

    metadata: str

    images: OfferDefinitionImages

    descriptions: OfferDefinitionDescriptions

    obtain: OfferDefinitionObtain

class OfferDefinition(RequiredOfferDefinition, OptionalOfferDefinition):
    pass
