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

from beamable_python_sdk.pydantic.client_permission import ClientPermission
from beamable_python_sdk.pydantic.event_group_rewards import EventGroupRewards
from beamable_python_sdk.pydantic.event_phase import EventPhase
from beamable_python_sdk.pydantic.event_reward_item import EventRewardItem
from beamable_python_sdk.pydantic.event_stores import EventStores
from beamable_python_sdk.pydantic.leaderboard_cohort_settings import LeaderboardCohortSettings
from beamable_python_sdk.pydantic.schedule import Schedule

class Event(BaseModel):
    name: typing.Optional[str] = Field(None, alias='name')

    start_date: typing.Optional[str] = Field(None, alias='start_date')

    phases: typing.Optional[typing.List[EventPhase]] = Field(None, alias='phases')

    partition_size: typing.Optional[int] = Field(None, alias='partition_size')

    group_rewards: typing.Optional[EventGroupRewards] = Field(None, alias='group_rewards')

    cohort_settings: typing.Optional[LeaderboardCohortSettings] = Field(None, alias='cohortSettings')

    permissions: typing.Optional[ClientPermission] = Field(None, alias='permissions')

    stores: typing.Optional[EventStores] = Field(None, alias='stores')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    score_rewards: typing.Optional[typing.List[EventRewardItem]] = Field(None, alias='score_rewards')

    schedule: typing.Optional[Schedule] = Field(None, alias='schedule')

    rank_rewards: typing.Optional[typing.List[EventRewardItem]] = Field(None, alias='rank_rewards')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
