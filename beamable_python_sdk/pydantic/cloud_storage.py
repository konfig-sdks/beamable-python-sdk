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


class CloudStorage(BaseModel):
    stype: int = Field(alias='stype')

    sid: int = Field(alias='sid')

    version: typing.Optional[int] = Field(None, alias='version')

    retrieved: typing.Optional[int] = Field(None, alias='retrieved')

    unique_identifier: typing.Optional[str] = Field(None, alias='uniqueIdentifier')

    data: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='data')

    ref: typing.Optional[str] = Field(None, alias='ref')

    added: typing.Optional[int] = Field(None, alias='added')

    updated: typing.Optional[int] = Field(None, alias='updated')

    expiration: typing.Optional[int] = Field(None, alias='expiration')

    gt: typing.Optional[int] = Field(None, alias='gt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
