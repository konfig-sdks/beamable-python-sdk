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

from beamable_python_sdk.pydantic.session_language_context import SessionLanguageContext
from beamable_python_sdk.pydantic.start_session_request_custom_params import StartSessionRequestCustomParams
from beamable_python_sdk.pydantic.start_session_request_device_params import StartSessionRequestDeviceParams

class StartSessionRequest(BaseModel):
    source: typing.Optional[str] = Field(None, alias='source')

    custom_params: typing.Optional[StartSessionRequestCustomParams] = Field(None, alias='customParams')

    shard: typing.Optional[str] = Field(None, alias='shard')

    locale: typing.Optional[str] = Field(None, alias='locale')

    device_params: typing.Optional[StartSessionRequestDeviceParams] = Field(None, alias='deviceParams')

    language: typing.Optional[SessionLanguageContext] = Field(None, alias='language')

    time: typing.Optional[int] = Field(None, alias='time')

    platform: typing.Optional[str] = Field(None, alias='platform')

    gamer: typing.Optional[int] = Field(None, alias='gamer')

    device: typing.Optional[str] = Field(None, alias='device')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
