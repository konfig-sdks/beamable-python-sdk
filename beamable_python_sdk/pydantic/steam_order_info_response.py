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

from beamable_python_sdk.pydantic.steam_order_info_item import SteamOrderInfoItem

class SteamOrderInfoResponse(BaseModel):
    transid: int = Field(alias='transid')

    orderid: int = Field(alias='orderid')

    steamid: int = Field(alias='steamid')

    usstate: typing.Optional[str] = Field(None, alias='usstate')

    items: typing.Optional[typing.List[SteamOrderInfoItem]] = Field(None, alias='items')

    country: typing.Optional[str] = Field(None, alias='country')

    timecreated: typing.Optional[str] = Field(None, alias='timecreated')

    status: typing.Optional[str] = Field(None, alias='status')

    currency: typing.Optional[str] = Field(None, alias='currency')

    time: typing.Optional[str] = Field(None, alias='time')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
