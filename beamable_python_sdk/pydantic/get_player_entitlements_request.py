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


class GetPlayerEntitlementsRequest(BaseModel):
    gt: int = Field(alias='gt')

    state: typing.Optional[str] = Field(None, alias='state')

    skip: typing.Optional[int] = Field(None, alias='skip')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    icw: typing.Optional[bool] = Field(None, alias='icw')

    spec: typing.Optional[str] = Field(None, alias='spec')

    limit: typing.Optional[int] = Field(None, alias='limit')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
