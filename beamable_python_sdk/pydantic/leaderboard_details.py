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

from beamable_python_sdk.pydantic.leader_board_view import LeaderBoardView
from beamable_python_sdk.pydantic.order_rules import OrderRules

class LeaderboardDetails(BaseModel):
    number_of_entries: int = Field(alias='numberOfEntries')

    lbid: typing.Optional[str] = Field(None, alias='lbid')

    orules: typing.Optional[OrderRules] = Field(None, alias='orules')

    full_name: typing.Optional[str] = Field(None, alias='fullName')

    view: typing.Optional[LeaderBoardView] = Field(None, alias='view')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
