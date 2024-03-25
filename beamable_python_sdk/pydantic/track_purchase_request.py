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

class TrackPurchaseRequest(BaseModel):
    price_in_local_currency: typing.Union[int, float] = Field(alias='priceInLocalCurrency')

    sku_name: typing.Optional[str] = Field(None, alias='skuName')

    sku_product_id: typing.Optional[str] = Field(None, alias='skuProductId')

    store: typing.Optional[str] = Field(None, alias='store')

    obtain_items: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='obtainItems')

    obtain_currency: typing.Optional[typing.List[CurrencyChange]] = Field(None, alias='obtainCurrency')

    purchase_id: typing.Optional[str] = Field(None, alias='purchaseId')

    iso_currency_symbol: typing.Optional[str] = Field(None, alias='isoCurrencySymbol')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
