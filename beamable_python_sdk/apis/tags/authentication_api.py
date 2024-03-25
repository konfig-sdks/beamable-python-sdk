# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.basic_auth_token.get import GetToken
from beamable_python_sdk.paths.basic_auth_token.post import RequestToken
from beamable_python_sdk.paths.basic_payments_steam_auth.post import SteamPostAuth
from beamable_python_sdk.apis.tags.authentication_api_raw import AuthenticationApiRaw


class AuthenticationApi(
    GetToken,
    RequestToken,
    SteamPostAuth,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AuthenticationApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AuthenticationApiRaw(api_client)
