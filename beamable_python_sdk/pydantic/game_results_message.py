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

from beamable_python_sdk.pydantic.currency_change import CurrencyChange
from beamable_python_sdk.pydantic.delta_score_by_leader_board_id import DeltaScoreByLeaderBoardId
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest

class GameResultsMessage(BaseModel):
    cheating_detected: bool = Field(alias='cheatingDetected')

    delta_scores: typing.Optional[typing.List[DeltaScoreByLeaderBoardId]] = Field(None, alias='deltaScores')

    currencies_granted: typing.Optional[typing.List[CurrencyChange]] = Field(None, alias='currenciesGranted')

    items_granted: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='itemsGranted')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
