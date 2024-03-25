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

from beamable_python_sdk.pydantic.entitlement_claim_window import EntitlementClaimWindow
from beamable_python_sdk.pydantic.entitlement_history import EntitlementHistory

class Entitlement(BaseModel):
    gamer_tag: int = Field(alias='gamerTag')

    updated: int = Field(alias='updated')

    cwin_secs_till_open: typing.Optional[int] = Field(None, alias='cwinSecsTillOpen')

    history: typing.Optional[EntitlementHistory] = Field(None, alias='history')

    state: typing.Optional[str] = Field(None, alias='state')

    uuid: typing.Optional[str] = Field(None, alias='uuid')

    cwin: typing.Optional[EntitlementClaimWindow] = Field(None, alias='cwin')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    specialized: typing.Optional[str] = Field(None, alias='specialized')

    cwin_secs_till_close: typing.Optional[int] = Field(None, alias='cwinSecsTillClose')

    ttl: typing.Optional[int] = Field(None, alias='ttl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
