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

from beamable_python_sdk.pydantic.cohort_requirement import CohortRequirement
from beamable_python_sdk.pydantic.entitlement_requirement import EntitlementRequirement
from beamable_python_sdk.pydantic.listing_button_text import ListingButtonText
from beamable_python_sdk.pydantic.listing_client_data import ListingClientData
from beamable_python_sdk.pydantic.offer_requirement import OfferRequirement
from beamable_python_sdk.pydantic.period import Period
from beamable_python_sdk.pydantic.player_stat_requirement import PlayerStatRequirement
from beamable_python_sdk.pydantic.price import Price

class Listing(BaseModel):
    cohort_requirements: typing.Optional[typing.List[CohortRequirement]] = Field(None, alias='cohortRequirements')

    offer_symbol: typing.Optional[str] = Field(None, alias='offerSymbol')

    purchase_limit: typing.Optional[int] = Field(None, alias='purchaseLimit')

    price: typing.Optional[Price] = Field(None, alias='price')

    player_stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = Field(None, alias='playerStatRequirements')

    button_text: typing.Optional[ListingButtonText] = Field(None, alias='buttonText')

    entitlement_requirements: typing.Optional[typing.List[EntitlementRequirement]] = Field(None, alias='entitlementRequirements')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    client_data: typing.Optional[ListingClientData] = Field(None, alias='clientData')

    active_duration_cool_down_seconds: typing.Optional[int] = Field(None, alias='activeDurationCoolDownSeconds')

    active_duration_seconds: typing.Optional[int] = Field(None, alias='activeDurationSeconds')

    active_duration_purchase_limit: typing.Optional[int] = Field(None, alias='activeDurationPurchaseLimit')

    offer_requirements: typing.Optional[typing.List[OfferRequirement]] = Field(None, alias='offerRequirements')

    active_period: typing.Optional[Period] = Field(None, alias='activePeriod')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
