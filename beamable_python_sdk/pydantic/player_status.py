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

from beamable_python_sdk.pydantic.tournament_reward import TournamentReward

class PlayerStatus(BaseModel):
    last_update_cycle: int = Field(alias='lastUpdateCycle')

    stage: int = Field(alias='stage')

    tier: int = Field(alias='tier')

    player_id: int = Field(alias='playerId')

    tournament_id: typing.Optional[str] = Field(None, alias='tournamentId')

    unclaimed_rewards: typing.Optional[typing.List[TournamentReward]] = Field(None, alias='unclaimedRewards')

    content_id: typing.Optional[str] = Field(None, alias='contentId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
