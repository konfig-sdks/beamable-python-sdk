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


class SubscriberDetailsResponse(BaseModel):
    custom_channel_prefix: typing.Optional[str] = Field(None, alias='customChannelPrefix')

    player_for_realm_channel: typing.Optional[str] = Field(None, alias='playerForRealmChannel')

    authentication_key: typing.Optional[str] = Field(None, alias='authenticationKey')

    game_global_notification_channel: typing.Optional[str] = Field(None, alias='gameGlobalNotificationChannel')

    game_notification_channel: typing.Optional[str] = Field(None, alias='gameNotificationChannel')

    subscribe_key: typing.Optional[str] = Field(None, alias='subscribeKey')

    player_channel: typing.Optional[str] = Field(None, alias='playerChannel')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
