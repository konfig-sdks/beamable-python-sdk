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

from beamable_python_sdk.pydantic.client_data_entry import ClientDataEntry
from beamable_python_sdk.pydantic.player_listing_view_client_data import PlayerListingViewClientData
from beamable_python_sdk.pydantic.player_offer_view import PlayerOfferView

class PlayerListingView(BaseModel):
    seconds_active: int = Field(alias='secondsActive')

    query_after_purchase: bool = Field(alias='queryAfterPurchase')

    active: bool = Field(alias='active')

    client_data_list: typing.Optional[typing.List[ClientDataEntry]] = Field(None, alias='clientDataList')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    client_data: typing.Optional[PlayerListingViewClientData] = Field(None, alias='clientData')

    cooldown: typing.Optional[int] = Field(None, alias='cooldown')

    offer: typing.Optional[PlayerOfferView] = Field(None, alias='offer')

    purchases_remain: typing.Optional[int] = Field(None, alias='purchasesRemain')

    seconds_remain: typing.Optional[int] = Field(None, alias='secondsRemain')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
