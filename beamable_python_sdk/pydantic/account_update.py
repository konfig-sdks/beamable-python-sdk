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

from beamable_python_sdk.pydantic.gamer_tag_association import GamerTagAssociation

class AccountUpdate(BaseModel):
    has_third_party_token: bool = Field(alias='hasThirdPartyToken')

    third_party: typing.Optional[str] = Field(None, alias='thirdParty')

    country: typing.Optional[str] = Field(None, alias='country')

    language: typing.Optional[str] = Field(None, alias='language')

    gamer_tag_assoc: typing.Optional[GamerTagAssociation] = Field(None, alias='gamerTagAssoc')

    token: typing.Optional[str] = Field(None, alias='token')

    device_id: typing.Optional[str] = Field(None, alias='deviceId')

    user_name: typing.Optional[str] = Field(None, alias='userName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
