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

from beamable_python_sdk.pydantic.date_time import DateTime
from beamable_python_sdk.pydantic.listing import Listing

class Store(BaseModel):
    store_with_annotations$default$3_: bool = Field(alias='storeWithAnnotations$default$3')

    title: typing.Optional[str] = Field(None, alias='title')

    active_listing_limit: typing.Optional[int] = Field(None, alias='activeListingLimit')

    choose: typing.Optional[int] = Field(None, alias='choose')

    listings: typing.Optional[typing.List[Listing]] = Field(None, alias='listings')

    show_inactive_listings: typing.Optional[bool] = Field(None, alias='showInactiveListings')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    refresh_time: typing.Optional[int] = Field(None, alias='refreshTime')

    store_with_annotations$default$2_: typing.Optional[DateTime] = Field(None, alias='storeWithAnnotations$default$2')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
