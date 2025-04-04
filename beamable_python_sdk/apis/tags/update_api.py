# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.basic_payments_facebook_update.get import FacebookPaymentsUpdate
from beamable_python_sdk.paths.basic_payments_facebook_update.post import FacebookPaymentsUpdate0
from beamable_python_sdk.apis.tags.update_api_raw import UpdateApiRaw


class UpdateApi(
    FacebookPaymentsUpdate,
    FacebookPaymentsUpdate0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UpdateApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UpdateApiRaw(api_client)
