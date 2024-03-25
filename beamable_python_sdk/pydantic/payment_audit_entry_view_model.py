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
from beamable_python_sdk.pydantic.entitlement_generator import EntitlementGenerator
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest
from beamable_python_sdk.pydantic.payment_details_entry_view_model import PaymentDetailsEntryViewModel
from beamable_python_sdk.pydantic.payment_history_entry_view_model import PaymentHistoryEntryViewModel

class PaymentAuditEntryViewModel(BaseModel):
    providerid: str = Field(alias='providerid')

    history: typing.List[PaymentHistoryEntryViewModel] = Field(alias='history')

    txid: int = Field(alias='txid')

    providername: str = Field(alias='providername')

    txstate: str = Field(alias='txstate')

    entitlements: typing.List[EntitlementGenerator] = Field(alias='entitlements')

    details: PaymentDetailsEntryViewModel = Field(alias='details')

    gt: int = Field(alias='gt')

    version: typing.Optional[str] = Field(None, alias='version')

    obtain_items: typing.Optional[typing.List[ItemCreateRequest]] = Field(None, alias='obtainItems')

    updated: typing.Optional[int] = Field(None, alias='updated')

    obtain_currency: typing.Optional[typing.List[CurrencyChange]] = Field(None, alias='obtainCurrency')

    replay_guard_value: typing.Optional[str] = Field(None, alias='replayGuardValue')

    created: typing.Optional[int] = Field(None, alias='created')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
