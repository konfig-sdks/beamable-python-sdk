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

from beamable_python_sdk.type.local_date import LocalDate
from beamable_python_sdk.type.payment_total import PaymentTotal
from beamable_python_sdk.type.session_history_response_payments import SessionHistoryResponsePayments
from beamable_python_sdk.type.session_history_response_sessions import SessionHistoryResponseSessions

class RequiredSessionHistoryResponse(TypedDict):
    daysPlayed: int

class OptionalSessionHistoryResponse(TypedDict, total=False):
    payments: SessionHistoryResponsePayments

    totalPaid: typing.List[PaymentTotal]

    sessions: SessionHistoryResponseSessions

    date: LocalDate

    installDate: str

class SessionHistoryResponse(RequiredSessionHistoryResponse, OptionalSessionHistoryResponse):
    pass
