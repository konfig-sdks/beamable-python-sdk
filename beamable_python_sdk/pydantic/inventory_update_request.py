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

from beamable_python_sdk.pydantic.inventory_update_request_currencies import InventoryUpdateRequestCurrencies
from beamable_python_sdk.pydantic.inventory_update_request_currency_content_ids import InventoryUpdateRequestCurrencyContentIds
from beamable_python_sdk.pydantic.inventory_update_request_currency_properties import InventoryUpdateRequestCurrencyProperties
from beamable_python_sdk.pydantic.inventory_update_request_item_content_ids import InventoryUpdateRequestItemContentIds
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest
from beamable_python_sdk.pydantic.item_delete_request import ItemDeleteRequest
from beamable_python_sdk.pydantic.item_update_request import ItemUpdateRequest

class InventoryUpdateRequest(BaseModel):
    empty: bool = Field(alias='empty')

    currency_content_ids: InventoryUpdateRequestCurrencyContentIds = Field(alias='currencyContentIds')

    item_content_ids: InventoryUpdateRequestItemContentIds = Field(alias='itemContentIds')

    currencies: typing.Optional[InventoryUpdateRequestCurrencies] = Field(None, alias='currencies')

    currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = Field(None, alias='currencyProperties')

    apply_vip_bonus: typing.Optional[bool] = Field(None, alias='applyVipBonus')

    update_items: typing.Optional[typing.List[ItemUpdateRequest]] = Field(None, alias='updateItems')

    new_items: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='newItems')

    transaction: typing.Optional[str] = Field(None, alias='transaction')

    delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = Field(None, alias='deleteItems')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
