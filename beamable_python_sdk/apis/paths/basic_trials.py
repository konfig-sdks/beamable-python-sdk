from beamable_python_sdk.paths.basic_trials.get import ApiForget
from beamable_python_sdk.paths.basic_trials.post import ApiForpost
from beamable_python_sdk.paths.basic_trials.delete import ApiFordelete


class BasicTrials(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
