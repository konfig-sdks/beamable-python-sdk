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

from beamable_python_sdk.type.cohort_requirement import CohortRequirement
from beamable_python_sdk.type.entitlement_requirement import EntitlementRequirement
from beamable_python_sdk.type.listing_button_text import ListingButtonText
from beamable_python_sdk.type.listing_client_data import ListingClientData
from beamable_python_sdk.type.offer_requirement import OfferRequirement
from beamable_python_sdk.type.period import Period
from beamable_python_sdk.type.player_stat_requirement import PlayerStatRequirement
from beamable_python_sdk.type.price import Price

class RequiredListing(TypedDict):
    pass

class OptionalListing(TypedDict, total=False):
    cohortRequirements: typing.List[CohortRequirement]

    offerSymbol: str

    purchaseLimit: int

    price: Price

    playerStatRequirements: typing.List[PlayerStatRequirement]

    buttonText: ListingButtonText

    entitlementRequirements: typing.List[EntitlementRequirement]

    symbol: str

    clientData: ListingClientData

    activeDurationCoolDownSeconds: int

    activeDurationSeconds: int

    activeDurationPurchaseLimit: int

    offerRequirements: typing.List[OfferRequirement]

    activePeriod: Period

class Listing(RequiredListing, OptionalListing):
    pass
