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

from beamable_python_sdk.pydantic.pvp_reward_definition import PvpRewardDefinition

class PvpDefinition(BaseModel):
    state: int = Field(alias='state')

    description: typing.Optional[str] = Field(None, alias='description')

    next_reward: typing.Optional[int] = Field(None, alias='nextReward')

    lbid: typing.Optional[str] = Field(None, alias='lbid')

    idle_days: typing.Optional[int] = Field(None, alias='idleDays')

    cron: typing.Optional[str] = Field(None, alias='cron')

    reward_definition: typing.Optional[PvpRewardDefinition] = Field(None, alias='rewardDefinition')

    protected_ranks: typing.Optional[int] = Field(None, alias='protectedRanks')

    min_players: typing.Optional[int] = Field(None, alias='minPlayers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
