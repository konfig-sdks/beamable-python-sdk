# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.basic_legacy_timers.post import CreateLegacyTimerRaw
from beamable_python_sdk.paths.basic_legacy_timers.delete import DeleteLegacyTimersRaw
from beamable_python_sdk.paths.basic_legacy_timers_defs.get import GetLegacyTimersRaw
from beamable_python_sdk.paths.basic_legacy_timers.get import GetLegacyTimers0Raw


class TimerApiRaw(
    CreateLegacyTimerRaw,
    DeleteLegacyTimersRaw,
    GetLegacyTimersRaw,
    GetLegacyTimers0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
