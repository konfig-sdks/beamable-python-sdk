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

from beamable_python_sdk.pydantic.token_response_scopes import TokenResponseScopes

class TokenResponse(BaseModel):
    access_token: str = Field(alias='access_token')

    expires_in: int = Field(alias='expires_in')

    refresh_token: str = Field(alias='refresh_token')

    token_type: str = Field(alias='token_type')

    scopes: typing.Optional[TokenResponseScopes] = Field(None, alias='scopes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
