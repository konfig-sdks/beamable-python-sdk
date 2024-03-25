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

from beamable_python_sdk.pydantic.token_request_wrapper_scope import TokenRequestWrapperScope

class TokenRequestWrapper(BaseModel):
    username: typing.Optional[str] = Field(None, alias='username')

    scope: typing.Optional[TokenRequestWrapperScope] = Field(None, alias='scope')

    refresh_token: typing.Optional[str] = Field(None, alias='refresh_token')

    third_party: typing.Optional[str] = Field(None, alias='third_party')

    redirect_uri: typing.Optional[str] = Field(None, alias='redirect_uri')

    client_id: typing.Optional[str] = Field(None, alias='client_id')

    code: typing.Optional[str] = Field(None, alias='code')

    token: typing.Optional[str] = Field(None, alias='token')

    customer_scoped: typing.Optional[bool] = Field(None, alias='customerScoped')

    grant_type: typing.Optional[str] = Field(None, alias='grant_type')

    password: typing.Optional[str] = Field(None, alias='password')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
