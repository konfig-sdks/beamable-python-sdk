# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.basic_payments_steam_prices.get import GetSteamPrices
from beamable_python_sdk.apis.tags.price_api_raw import PriceApiRaw


class PriceApi(
    GetSteamPrices,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PriceApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PriceApiRaw(api_client)
