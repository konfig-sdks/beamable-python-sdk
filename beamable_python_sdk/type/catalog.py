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

from beamable_python_sdk.type.offer_definition import OfferDefinition
from beamable_python_sdk.type.sku_definitions import SKUDefinitions
from beamable_python_sdk.type.store import Store

RequiredCatalog = TypedDict("RequiredCatalog", {
    "version": int,
    })

OptionalCatalog = TypedDict("OptionalCatalog", {
    "listingInfo$default$2": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    "offerDefinitions": typing.List[OfferDefinition],

    "stores": typing.List[Store],

    "listingInfo$default$3": SKUDefinitions,

    "created": int,
    }, total=False)

class Catalog(RequiredCatalog, OptionalCatalog):
    pass
