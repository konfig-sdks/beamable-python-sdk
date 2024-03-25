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

from beamable_python_sdk.pydantic.third_party_association_meta import ThirdPartyAssociationMeta

class ThirdPartyAssociation(BaseModel):
    name: str = Field(alias='name')

    user_app_id: str = Field(alias='userAppId')

    meta: ThirdPartyAssociationMeta = Field(alias='meta')

    app_id: str = Field(alias='appId')

    email: typing.Optional[str] = Field(None, alias='email')

    user_business_id: typing.Optional[str] = Field(None, alias='userBusinessId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
