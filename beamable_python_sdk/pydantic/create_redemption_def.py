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

from beamable_python_sdk.pydantic.create_redemption_def_whitelist import CreateRedemptionDefWhitelist
from beamable_python_sdk.pydantic.entitlement_generator import EntitlementGenerator
from beamable_python_sdk.pydantic.player_reward import PlayerReward

class CreateRedemptionDef(BaseModel):
    max_per_user: int = Field(alias='maxPerUser')

    description: typing.Optional[str] = Field(None, alias='description')

    name: typing.Optional[str] = Field(None, alias='name')

    time_expires: typing.Optional[int] = Field(None, alias='timeExpires')

    reward: typing.Optional[EntitlementGenerator] = Field(None, alias='reward')

    gift: typing.Optional[PlayerReward] = Field(None, alias='gift')

    whitelist: typing.Optional[CreateRedemptionDefWhitelist] = Field(None, alias='whitelist')

    classification: typing.Optional[str] = Field(None, alias='classification')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
