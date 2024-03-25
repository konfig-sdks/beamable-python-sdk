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

from beamable_python_sdk.pydantic.token_scopes import TokenScopes

class Token(BaseModel):
    cid: int = Field(alias='cid')

    created: int = Field(alias='created')

    gamer_tag: typing.Optional[int] = Field(None, alias='gamerTag')

    scopes: typing.Optional[TokenScopes] = Field(None, alias='scopes')

    account_id: typing.Optional[int] = Field(None, alias='accountId')

    pid: typing.Optional[str] = Field(None, alias='pid')

    expires_ms: typing.Optional[int] = Field(None, alias='expiresMs')

    token: typing.Optional[str] = Field(None, alias='token')

    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
