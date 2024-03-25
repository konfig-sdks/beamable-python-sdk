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

from beamable_python_sdk.pydantic.local_date import LocalDate
from beamable_python_sdk.pydantic.payment_total import PaymentTotal
from beamable_python_sdk.pydantic.session_history_response_payments import SessionHistoryResponsePayments
from beamable_python_sdk.pydantic.session_history_response_sessions import SessionHistoryResponseSessions

class SessionHistoryResponse(BaseModel):
    days_played: int = Field(alias='daysPlayed')

    payments: typing.Optional[SessionHistoryResponsePayments] = Field(None, alias='payments')

    total_paid: typing.Optional[typing.List[PaymentTotal]] = Field(None, alias='totalPaid')

    sessions: typing.Optional[SessionHistoryResponseSessions] = Field(None, alias='sessions')

    date: typing.Optional[LocalDate] = Field(None, alias='date')

    install_date: typing.Optional[str] = Field(None, alias='installDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
