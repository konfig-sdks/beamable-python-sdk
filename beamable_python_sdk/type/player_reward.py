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

from beamable_python_sdk.type.currency_change_reward import CurrencyChangeReward
from beamable_python_sdk.type.item_create_request import ItemCreateRequest
from beamable_python_sdk.type.new_item_reward import NewItemReward
from beamable_python_sdk.type.player_reward_add_currency_map import PlayerRewardAddCurrencyMap
from beamable_python_sdk.type.webhook_reward import WebhookReward

class RequiredPlayerReward(TypedDict):
    pass

class OptionalPlayerReward(TypedDict, total=False):
    description: str

    addItemRequests: typing.List[ItemCreateRequest]

    changeCurrencies: typing.List[CurrencyChangeReward]

    callWebhooks: typing.List[WebhookReward]

    addItems: typing.List[NewItemReward]

    applyVipBonus: bool

    addCurrencyMap: PlayerRewardAddCurrencyMap

class PlayerReward(RequiredPlayerReward, OptionalPlayerReward):
    pass
