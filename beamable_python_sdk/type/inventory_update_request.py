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

from beamable_python_sdk.type.inventory_update_request_currencies import InventoryUpdateRequestCurrencies
from beamable_python_sdk.type.inventory_update_request_currency_content_ids import InventoryUpdateRequestCurrencyContentIds
from beamable_python_sdk.type.inventory_update_request_currency_properties import InventoryUpdateRequestCurrencyProperties
from beamable_python_sdk.type.inventory_update_request_item_content_ids import InventoryUpdateRequestItemContentIds
from beamable_python_sdk.type.item_create_request import ItemCreateRequest
from beamable_python_sdk.type.item_delete_request import ItemDeleteRequest
from beamable_python_sdk.type.item_update_request import ItemUpdateRequest

class RequiredInventoryUpdateRequest(TypedDict):
    empty: bool

    currencyContentIds: InventoryUpdateRequestCurrencyContentIds

    itemContentIds: InventoryUpdateRequestItemContentIds

class OptionalInventoryUpdateRequest(TypedDict, total=False):
    currencies: InventoryUpdateRequestCurrencies

    currencyProperties: InventoryUpdateRequestCurrencyProperties

    applyVipBonus: bool

    updateItems: typing.List[ItemUpdateRequest]

    newItems: typing.List[ItemCreateRequest]

    transaction: str

    deleteItems: typing.List[ItemDeleteRequest]

class InventoryUpdateRequest(RequiredInventoryUpdateRequest, OptionalInventoryUpdateRequest):
    pass
