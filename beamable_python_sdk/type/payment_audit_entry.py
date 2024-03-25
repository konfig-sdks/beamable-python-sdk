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
from beamable_python_sdk.type.entitlement_generator import EntitlementGenerator
from beamable_python_sdk.type.in_flight_message import InFlightMessage
from beamable_python_sdk.type.item_create_request import ItemCreateRequest
from beamable_python_sdk.type.payment_details_entry import PaymentDetailsEntry
from beamable_python_sdk.type.payment_history_entry import PaymentHistoryEntry

class RequiredPaymentAuditEntry(TypedDict):
    txid: int

    gt: int

class OptionalPaymentAuditEntry(TypedDict, total=False):
    version: str

    inFlight: typing.List[InFlightMessage]

    providerid: str

    history: typing.List[PaymentHistoryEntry]

    providername: str

    obtainItems: typing.List[ItemCreateRequest]

    txstate: str

    updated: int

    obtainCurrency: typing.List[CurrencyChange]

    entitlements: typing.List[EntitlementGenerator]

    details: PaymentDetailsEntry

    replayGuardValue: str

    created: int

class PaymentAuditEntry(RequiredPaymentAuditEntry, OptionalPaymentAuditEntry):
    pass
