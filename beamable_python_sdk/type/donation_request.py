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

from beamable_python_sdk.type.currency import Currency
from beamable_python_sdk.type.donation_entry import DonationEntry

class RequiredDonationRequest(TypedDict):
    timeRequested: int

    satisfied: bool

    playerId: int

class OptionalDonationRequest(TypedDict, total=False):
    progress: typing.List[DonationEntry]

    currency: Currency

class DonationRequest(RequiredDonationRequest, OptionalDonationRequest):
    pass
