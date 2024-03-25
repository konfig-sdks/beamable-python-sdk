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

from beamable_python_sdk.pydantic.notification_request_data_message_params import NotificationRequestDataMessageParams
from beamable_python_sdk.pydantic.notification_request_data_meta import NotificationRequestDataMeta

class NotificationRequestData(BaseModel):
    message_params: typing.Optional[NotificationRequestDataMessageParams] = Field(None, alias='messageParams')

    channel: typing.Optional[str] = Field(None, alias='channel')

    message_key: typing.Optional[str] = Field(None, alias='messageKey')

    context: typing.Optional[str] = Field(None, alias='context')

    shard: typing.Optional[str] = Field(None, alias='shard')

    meta: typing.Optional[NotificationRequestDataMeta] = Field(None, alias='meta')

    message_full: typing.Optional[str] = Field(None, alias='messageFull')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
