from beamable_python_sdk.paths.basic_legacy_timers.get import ApiForget
from beamable_python_sdk.paths.basic_legacy_timers.post import ApiForpost
from beamable_python_sdk.paths.basic_legacy_timers.delete import ApiFordelete


class BasicLegacyTimers(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
