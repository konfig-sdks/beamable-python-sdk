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
from beamable_python_sdk.type.event import Event
from beamable_python_sdk.type.event_phase_runtime import EventPhaseRuntime
from beamable_python_sdk.type.in_flight_message import InFlightMessage

class RequiredEventObjectData(TypedDict):
    running: bool

    done: bool

class OptionalEventObjectData(TypedDict, total=False):
    inFlight: typing.List[InFlightMessage]

    startTime: int

    rootEventId: str

    state: str

    phase: EventPhaseRuntime

    permissions: ClientPermission

    lastChildEventId: str

    id: str

    origin: str

    content: Event

    leaderboardId: str

class EventObjectData(RequiredEventObjectData, OptionalEventObjectData):
    pass
