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


class User(BaseModel):
    gamer_tag: int = Field(alias='gamerTag')

    id: int = Field(alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    email: typing.Optional[str] = Field(None, alias='email')

    username: typing.Optional[str] = Field(None, alias='username')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    cid: typing.Optional[str] = Field(None, alias='cid')

    lang: typing.Optional[str] = Field(None, alias='lang')

    heartbeat: typing.Optional[int] = Field(None, alias='heartbeat')

    password: typing.Optional[str] = Field(None, alias='password')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
