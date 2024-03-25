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

from beamable_python_sdk.type.event_player_phase_view import EventPlayerPhaseView
from beamable_python_sdk.type.event_player_reward import EventPlayerReward

class RequiredEventPlayerStateView(TypedDict):
    running: bool

    rank: int

    score: typing.Union[int, float]

    secondsRemaining: int

class OptionalEventPlayerStateView(TypedDict, total=False):
    name: str

    allPhases: typing.List[EventPlayerPhaseView]

    currentPhase: EventPlayerPhaseView

    id: str

    leaderboardId: str

    rankRewards: typing.List[EventPlayerReward]

    scoreRewards: typing.List[EventPlayerReward]

class EventPlayerStateView(RequiredEventPlayerStateView, OptionalEventPlayerStateView):
    pass
