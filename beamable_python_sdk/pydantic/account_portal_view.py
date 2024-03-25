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

from beamable_python_sdk.pydantic.account_portal_view_scopes import AccountPortalViewScopes
from beamable_python_sdk.pydantic.account_portal_view_third_party_app_associations import AccountPortalViewThirdPartyAppAssociations
from beamable_python_sdk.pydantic.role_mapping import RoleMapping

class AccountPortalView(BaseModel):
    scopes: AccountPortalViewScopes = Field(alias='scopes')

    id: int = Field(alias='id')

    third_party_app_associations: AccountPortalViewThirdPartyAppAssociations = Field(alias='thirdPartyAppAssociations')

    email: typing.Optional[str] = Field(None, alias='email')

    role_string: typing.Optional[str] = Field(None, alias='roleString')

    language: typing.Optional[str] = Field(None, alias='language')

    roles: typing.Optional[typing.List[RoleMapping]] = Field(None, alias='roles')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
