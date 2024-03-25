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

from beamable_python_sdk.type.stat_update_request_add import StatUpdateRequestAdd
from beamable_python_sdk.type.stat_update_request_set import StatUpdateRequestSet

class RequiredStatUpdateRequest(TypedDict):
    pass

class OptionalStatUpdateRequest(TypedDict, total=False):
    objectId: str

    set: StatUpdateRequestSet

    add: StatUpdateRequestAdd

    emitAnalytics: bool

class StatUpdateRequest(RequiredStatUpdateRequest, OptionalStatUpdateRequest):
    pass
