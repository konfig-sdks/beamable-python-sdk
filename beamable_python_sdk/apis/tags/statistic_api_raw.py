# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.basic_stats_batch.post import BatchPostRaw
from beamable_python_sdk.paths.basic_stats_client_batch.get import GetClientBatchStatsRaw
from beamable_python_sdk.paths.basic_stats_search.post import SearchDataRaw


class StatisticApiRaw(
    BatchPostRaw,
    GetClientBatchStatsRaw,
    SearchDataRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
