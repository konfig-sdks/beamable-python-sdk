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
from beamable_python_sdk.pydantic.event import Event
from beamable_python_sdk.pydantic.event_phase_runtime import EventPhaseRuntime
from beamable_python_sdk.pydantic.in_flight_message import InFlightMessage

class EventObjectData(BaseModel):
    running: bool = Field(alias='running')

    done: bool = Field(alias='done')

    in_flight: typing.Optional[typing.List[InFlightMessage]] = Field(None, alias='inFlight')

    start_time: typing.Optional[int] = Field(None, alias='startTime')

    root_event_id: typing.Optional[str] = Field(None, alias='rootEventId')

    state: typing.Optional[Literal["not-available"]] = Field(None, alias='state')

    phase: typing.Optional[EventPhaseRuntime] = Field(None, alias='phase')

    permissions: typing.Optional[ClientPermission] = Field(None, alias='permissions')

    last_child_event_id: typing.Optional[str] = Field(None, alias='lastChildEventId')

    id: typing.Optional[str] = Field(None, alias='id')

    origin: typing.Optional[str] = Field(None, alias='origin')

    content: typing.Optional[Event] = Field(None, alias='content')

    leaderboard_id: typing.Optional[str] = Field(None, alias='leaderboardId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
