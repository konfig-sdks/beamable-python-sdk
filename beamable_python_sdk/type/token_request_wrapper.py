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

from beamable_python_sdk.type.token_request_wrapper_scope import TokenRequestWrapperScope

class RequiredTokenRequestWrapper(TypedDict):
    pass

class OptionalTokenRequestWrapper(TypedDict, total=False):
    username: str

    scope: TokenRequestWrapperScope

    refresh_token: str

    third_party: str

    redirect_uri: str

    client_id: str

    code: str

    token: str

    customerScoped: bool

    grant_type: str

    password: str

class TokenRequestWrapper(RequiredTokenRequestWrapper, OptionalTokenRequestWrapper):
    pass
