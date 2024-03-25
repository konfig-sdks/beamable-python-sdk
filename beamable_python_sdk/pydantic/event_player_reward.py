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

from beamable_python_sdk.pydantic.event_inventory_pending_rewards import EventInventoryPendingRewards
from beamable_python_sdk.pydantic.event_inventory_reward_currency import EventInventoryRewardCurrency
from beamable_python_sdk.pydantic.event_inventory_reward_item import EventInventoryRewardItem
from beamable_python_sdk.pydantic.event_player_reward_pending_currency_rewards import EventPlayerRewardPendingCurrencyRewards
from beamable_python_sdk.pydantic.event_player_reward_pending_entitlement_rewards import EventPlayerRewardPendingEntitlementRewards
from beamable_python_sdk.pydantic.event_reward_obtain import EventRewardObtain
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest

class EventPlayerReward(BaseModel):
    min: typing.Union[int, float] = Field(alias='min')

    earned: bool = Field(alias='earned')

    claimed: bool = Field(alias='claimed')

    pending_inventory_rewards: typing.Optional[EventInventoryPendingRewards] = Field(None, alias='pendingInventoryRewards')

    currencies: typing.Optional[typing.List[EventInventoryRewardCurrency]] = Field(None, alias='currencies')

    pending_currency_rewards: typing.Optional[EventPlayerRewardPendingCurrencyRewards] = Field(None, alias='pendingCurrencyRewards')

    pending_item_rewards: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='pendingItemRewards')

    items: typing.Optional[typing.List[EventInventoryRewardItem]] = Field(None, alias='items')

    max: typing.Optional[typing.Union[int, float]] = Field(None, alias='max')

    pending_entitlement_rewards: typing.Optional[EventPlayerRewardPendingEntitlementRewards] = Field(None, alias='pendingEntitlementRewards')

    obtain: typing.Optional[typing.List[EventRewardObtain]] = Field(None, alias='obtain')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
