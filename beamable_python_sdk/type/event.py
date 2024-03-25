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

from beamable_python_sdk.type.client_permission import ClientPermission
from beamable_python_sdk.type.event_group_rewards import EventGroupRewards
from beamable_python_sdk.type.event_phase import EventPhase
from beamable_python_sdk.type.event_reward_item import EventRewardItem
from beamable_python_sdk.type.event_stores import EventStores
from beamable_python_sdk.type.leaderboard_cohort_settings import LeaderboardCohortSettings
from beamable_python_sdk.type.schedule import Schedule

class RequiredEvent(TypedDict):
    pass

class OptionalEvent(TypedDict, total=False):
    name: str

    start_date: str

    phases: typing.List[EventPhase]

    partition_size: int

    group_rewards: EventGroupRewards

    cohortSettings: LeaderboardCohortSettings

    permissions: ClientPermission

    stores: EventStores

    symbol: str

    score_rewards: typing.List[EventRewardItem]

    schedule: Schedule

    rank_rewards: typing.List[EventRewardItem]

class Event(RequiredEvent, OptionalEvent):
    pass
