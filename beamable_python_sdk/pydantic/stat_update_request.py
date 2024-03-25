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

from beamable_python_sdk.pydantic.stat_update_request_add import StatUpdateRequestAdd
from beamable_python_sdk.pydantic.stat_update_request_set import StatUpdateRequestSet

class StatUpdateRequest(BaseModel):
    object_id: typing.Optional[str] = Field(None, alias='objectId')

    set: typing.Optional[StatUpdateRequestSet] = Field(None, alias='set')

    add: typing.Optional[StatUpdateRequestAdd] = Field(None, alias='add')

    emit_analytics: typing.Optional[bool] = Field(None, alias='emitAnalytics')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
