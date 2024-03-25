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

from beamable_python_sdk.type.currency_change import CurrencyChange
from beamable_python_sdk.type.delta_score_by_leader_board_id import DeltaScoreByLeaderBoardId
from beamable_python_sdk.type.item_create_request import ItemCreateRequest

class RequiredGameResultsMessage(TypedDict):
    cheatingDetected: bool

class OptionalGameResultsMessage(TypedDict, total=False):
    deltaScores: typing.List[DeltaScoreByLeaderBoardId]

    currenciesGranted: typing.List[CurrencyChange]

    itemsGranted: typing.List[ItemCreateRequest]

class GameResultsMessage(RequiredGameResultsMessage, OptionalGameResultsMessage):
    pass
