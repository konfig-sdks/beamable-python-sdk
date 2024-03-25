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

from beamable_python_sdk.pydantic.currency_change_reward import CurrencyChangeReward
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest
from beamable_python_sdk.pydantic.new_item_reward import NewItemReward
from beamable_python_sdk.pydantic.player_reward_add_currency_map import PlayerRewardAddCurrencyMap
from beamable_python_sdk.pydantic.webhook_reward import WebhookReward

class PlayerReward(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    add_item_requests: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='addItemRequests')

    change_currencies: typing.Optional[typing.List[CurrencyChangeReward]] = Field(None, alias='changeCurrencies')

    call_webhooks: typing.Optional[typing.List[WebhookReward]] = Field(None, alias='callWebhooks')

    add_items: typing.Optional[typing.List[NewItemReward]] = Field(None, alias='addItems')

    apply_vip_bonus: typing.Optional[bool] = Field(None, alias='applyVipBonus')

    add_currency_map: typing.Optional[PlayerRewardAddCurrencyMap] = Field(None, alias='addCurrencyMap')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
