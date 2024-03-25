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

from beamable_python_sdk.pydantic.cohort_entry import CohortEntry
from beamable_python_sdk.pydantic.user import User

class GamerTag(BaseModel):
    tag: int = Field(alias='tag')

    alias: typing.Optional[str] = Field(None, alias='alias')

    added: typing.Optional[int] = Field(None, alias='added')

    trials: typing.Optional[typing.List[CohortEntry]] = Field(None, alias='trials')

    platform: typing.Optional[str] = Field(None, alias='platform')

    user: typing.Optional[User] = Field(None, alias='user')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
