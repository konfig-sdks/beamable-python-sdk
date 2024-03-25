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

from beamable_python_sdk.pydantic.event_player_phase_view import EventPlayerPhaseView
from beamable_python_sdk.pydantic.event_player_reward import EventPlayerReward

class EventPlayerStateView(BaseModel):
    running: bool = Field(alias='running')

    rank: int = Field(alias='rank')

    score: typing.Union[int, float] = Field(alias='score')

    seconds_remaining: int = Field(alias='secondsRemaining')

    name: typing.Optional[str] = Field(None, alias='name')

    all_phases: typing.Optional[typing.List[EventPlayerPhaseView]] = Field(None, alias='allPhases')

    current_phase: typing.Optional[EventPlayerPhaseView] = Field(None, alias='currentPhase')

    id: typing.Optional[str] = Field(None, alias='id')

    leaderboard_id: typing.Optional[str] = Field(None, alias='leaderboardId')

    rank_rewards: typing.Optional[typing.List[EventPlayerReward]] = Field(None, alias='rankRewards')

    score_rewards: typing.Optional[typing.List[EventPlayerReward]] = Field(None, alias='scoreRewards')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
