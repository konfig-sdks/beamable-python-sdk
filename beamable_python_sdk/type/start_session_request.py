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

from beamable_python_sdk.type.session_language_context import SessionLanguageContext
from beamable_python_sdk.type.start_session_request_custom_params import StartSessionRequestCustomParams
from beamable_python_sdk.type.start_session_request_device_params import StartSessionRequestDeviceParams

class RequiredStartSessionRequest(TypedDict):
    pass

class OptionalStartSessionRequest(TypedDict, total=False):
    source: str

    customParams: StartSessionRequestCustomParams

    shard: str

    locale: str

    deviceParams: StartSessionRequestDeviceParams

    language: SessionLanguageContext

    time: int

    platform: str

    gamer: int

    device: str

class StartSessionRequest(RequiredStartSessionRequest, OptionalStartSessionRequest):
    pass
