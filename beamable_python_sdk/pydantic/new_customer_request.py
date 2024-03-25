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


class NewCustomerRequest(BaseModel):
    project_name: str = Field(alias='projectName')

    email: str = Field(alias='email')

    password: str = Field(alias='password')

    customer_name: typing.Optional[str] = Field(None, alias='customerName')

    hierarchy: typing.Optional[bool] = Field(None, alias='hierarchy')

    alias: typing.Optional[str] = Field(None, alias='alias')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
