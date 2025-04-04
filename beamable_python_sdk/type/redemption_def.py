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

from beamable_python_sdk.type.entitlement_generator import EntitlementGenerator
from beamable_python_sdk.type.player_reward import PlayerReward
from beamable_python_sdk.type.redemption_def_whitelist import RedemptionDefWhitelist

class RequiredRedemptionDef(TypedDict):
    creatorGt: int

    timeCreated: int

    maxPerUser: int

    id: int

class OptionalRedemptionDef(TypedDict, total=False):
    description: str

    name: str

    timeExpires: int

    reward: EntitlementGenerator

    gift: PlayerReward

    whitelist: RedemptionDefWhitelist

    classification: str

class RedemptionDef(RequiredRedemptionDef, OptionalRedemptionDef):
    pass
