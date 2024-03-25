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


class RequiredGetActiveListingRequest(TypedDict):
    pass

class OptionalGetActiveListingRequest(TypedDict, total=False):
    listing: str

    store: str

    time: str

class GetActiveListingRequest(RequiredGetActiveListingRequest, OptionalGetActiveListingRequest):
    pass
