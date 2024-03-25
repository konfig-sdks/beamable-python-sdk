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

from beamable_python_sdk.type.cooked_timer_def import CookedTimerDef

class RequiredListTimersResponse(TypedDict):
    pass

class OptionalListTimersResponse(TypedDict, total=False):
    result: str

    timers: typing.List[CookedTimerDef]

class ListTimersResponse(RequiredListTimersResponse, OptionalListTimersResponse):
    pass
