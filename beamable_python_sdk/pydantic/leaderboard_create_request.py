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
from beamable_python_sdk.pydantic.leaderboard_create_request_derivatives import LeaderboardCreateRequestDerivatives

class LeaderboardCreateRequest(BaseModel):
    sharded: bool = Field(alias='sharded')

    freeze_time: typing.Optional[int] = Field(None, alias='freezeTime')

    derivatives: typing.Optional[LeaderboardCreateRequestDerivatives] = Field(None, alias='derivatives')

    score_name: typing.Optional[str] = Field(None, alias='scoreName')

    permissions: typing.Optional[ClientPermission] = Field(None, alias='permissions')

    max_entries: typing.Optional[int] = Field(None, alias='maxEntries')

    partitioned: typing.Optional[bool] = Field(None, alias='partitioned')

    ttl: typing.Optional[int] = Field(None, alias='ttl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
