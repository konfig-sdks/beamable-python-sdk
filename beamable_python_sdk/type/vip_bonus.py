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


class RequiredVipBonus(TypedDict):
    currency: str

    multiplier: typing.Union[int, float]

    roundToNearest: int

class OptionalVipBonus(TypedDict, total=False):
    pass

class VipBonus(RequiredVipBonus, OptionalVipBonus):
    pass
