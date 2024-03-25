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

from beamable_python_sdk.pydantic.currency_change import CurrencyChange
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest
from beamable_python_sdk.pydantic.player_offer_view_descriptions import PlayerOfferViewDescriptions
from beamable_python_sdk.pydantic.player_offer_view_images import PlayerOfferViewImages
from beamable_python_sdk.pydantic.player_offer_view_obtain import PlayerOfferViewObtain
from beamable_python_sdk.pydantic.player_offer_view_titles import PlayerOfferViewTitles
from beamable_python_sdk.pydantic.price import Price

class PlayerOfferView(BaseModel):
    coupons: int = Field(alias='coupons')

    price: typing.Optional[Price] = Field(None, alias='price')

    button_text: typing.Optional[str] = Field(None, alias='buttonText')

    titles: typing.Optional[PlayerOfferViewTitles] = Field(None, alias='titles')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    obtain_items: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='obtainItems')

    obtain_currency: typing.Optional[typing.List[CurrencyChange]] = Field(None, alias='obtainCurrency')

    images: typing.Optional[PlayerOfferViewImages] = Field(None, alias='images')

    descriptions: typing.Optional[PlayerOfferViewDescriptions] = Field(None, alias='descriptions')

    obtain: typing.Optional[PlayerOfferViewObtain] = Field(None, alias='obtain')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
