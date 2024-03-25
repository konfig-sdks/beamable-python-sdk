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

from beamable_python_sdk.type.currency_change import CurrencyChange
from beamable_python_sdk.type.item_create_request import ItemCreateRequest
from beamable_python_sdk.type.player_offer_view_descriptions import PlayerOfferViewDescriptions
from beamable_python_sdk.type.player_offer_view_images import PlayerOfferViewImages
from beamable_python_sdk.type.player_offer_view_obtain import PlayerOfferViewObtain
from beamable_python_sdk.type.player_offer_view_titles import PlayerOfferViewTitles
from beamable_python_sdk.type.price import Price

class RequiredPlayerOfferView(TypedDict):
    coupons: int

class OptionalPlayerOfferView(TypedDict, total=False):
    price: Price

    buttonText: str

    titles: PlayerOfferViewTitles

    symbol: str

    obtainItems: typing.List[ItemCreateRequest]

    obtainCurrency: typing.List[CurrencyChange]

    images: PlayerOfferViewImages

    descriptions: PlayerOfferViewDescriptions

    obtain: PlayerOfferViewObtain

class PlayerOfferView(RequiredPlayerOfferView, OptionalPlayerOfferView):
    pass
