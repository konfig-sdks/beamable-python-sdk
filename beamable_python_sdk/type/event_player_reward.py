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

from beamable_python_sdk.type.event_inventory_pending_rewards import EventInventoryPendingRewards
from beamable_python_sdk.type.event_inventory_reward_currency import EventInventoryRewardCurrency
from beamable_python_sdk.type.event_inventory_reward_item import EventInventoryRewardItem
from beamable_python_sdk.type.event_player_reward_pending_currency_rewards import EventPlayerRewardPendingCurrencyRewards
from beamable_python_sdk.type.event_player_reward_pending_entitlement_rewards import EventPlayerRewardPendingEntitlementRewards
from beamable_python_sdk.type.event_reward_obtain import EventRewardObtain
from beamable_python_sdk.type.item_create_request import ItemCreateRequest

class RequiredEventPlayerReward(TypedDict):
    min: typing.Union[int, float]

    earned: bool

    claimed: bool

class OptionalEventPlayerReward(TypedDict, total=False):
    pendingInventoryRewards: EventInventoryPendingRewards

    currencies: typing.List[EventInventoryRewardCurrency]

    pendingCurrencyRewards: EventPlayerRewardPendingCurrencyRewards

    pendingItemRewards: typing.List[ItemCreateRequest]

    items: typing.List[EventInventoryRewardItem]

    max: typing.Union[int, float]

    pendingEntitlementRewards: EventPlayerRewardPendingEntitlementRewards

    obtain: typing.List[EventRewardObtain]

class EventPlayerReward(RequiredEventPlayerReward, OptionalEventPlayerReward):
    pass
