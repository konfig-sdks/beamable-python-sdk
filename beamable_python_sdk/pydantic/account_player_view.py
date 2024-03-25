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

from beamable_python_sdk.pydantic.account_player_view_device_ids import AccountPlayerViewDeviceIds
from beamable_python_sdk.pydantic.account_player_view_scopes import AccountPlayerViewScopes
from beamable_python_sdk.pydantic.account_player_view_third_party_app_associations import AccountPlayerViewThirdPartyAppAssociations

class AccountPlayerView(BaseModel):
    device_ids: AccountPlayerViewDeviceIds = Field(alias='deviceIds')

    scopes: AccountPlayerViewScopes = Field(alias='scopes')

    id: int = Field(alias='id')

    third_party_app_associations: AccountPlayerViewThirdPartyAppAssociations = Field(alias='thirdPartyAppAssociations')

    email: typing.Optional[str] = Field(None, alias='email')

    language: typing.Optional[str] = Field(None, alias='language')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
