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


class PaymentDetailsEntry(BaseModel):
    quantity: int = Field(alias='quantity')

    price: int = Field(alias='price')

    reference: typing.Optional[str] = Field(None, alias='reference')

    name: typing.Optional[str] = Field(None, alias='name')

    sku: typing.Optional[str] = Field(None, alias='sku')

    subcategory: typing.Optional[str] = Field(None, alias='subcategory')

    gameplace: typing.Optional[str] = Field(None, alias='gameplace')

    local_price: typing.Optional[str] = Field(None, alias='localPrice')

    category: typing.Optional[str] = Field(None, alias='category')

    local_currency: typing.Optional[str] = Field(None, alias='localCurrency')

    provider_product_id: typing.Optional[str] = Field(None, alias='providerProductId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
