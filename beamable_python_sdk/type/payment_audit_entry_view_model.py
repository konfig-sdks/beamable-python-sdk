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
from beamable_python_sdk.type.item_create_request import ItemCreateRequest
from beamable_python_sdk.type.payment_details_entry_view_model import PaymentDetailsEntryViewModel
from beamable_python_sdk.type.payment_history_entry_view_model import PaymentHistoryEntryViewModel

class RequiredPaymentAuditEntryViewModel(TypedDict):
    providerid: str

    history: typing.List[PaymentHistoryEntryViewModel]

    txid: int

    providername: str

    txstate: str

    entitlements: typing.List[EntitlementGenerator]

    details: PaymentDetailsEntryViewModel

    gt: int

class OptionalPaymentAuditEntryViewModel(TypedDict, total=False):
    version: str

    obtainItems: typing.List[ItemCreateRequest]

    updated: int

    obtainCurrency: typing.List[CurrencyChange]

    replayGuardValue: str

    created: int

class PaymentAuditEntryViewModel(RequiredPaymentAuditEntryViewModel, OptionalPaymentAuditEntryViewModel):
    pass
