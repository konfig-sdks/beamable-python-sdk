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

from beamable_python_sdk.pydantic.account import Account
from beamable_python_sdk.pydantic.project import Project

class Customer(BaseModel):
    name: str = Field(alias='name')

    cid: int = Field(alias='cid')

    projects: typing.List[Project] = Field(alias='projects')

    accounts: typing.List[Account] = Field(alias='accounts')

    payment_status: typing.Optional[str] = Field(None, alias='paymentStatus')

    image: typing.Optional[str] = Field(None, alias='image')

    contact: typing.Optional[str] = Field(None, alias='contact')

    alias: typing.Optional[str] = Field(None, alias='alias')

    updated: typing.Optional[int] = Field(None, alias='updated')

    crm_link: typing.Optional[str] = Field(None, alias='crm_link')

    created: typing.Optional[int] = Field(None, alias='created')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
