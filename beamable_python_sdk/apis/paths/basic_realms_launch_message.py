from beamable_python_sdk.paths.basic_realms_launch_message.get import ApiForget
from beamable_python_sdk.paths.basic_realms_launch_message.post import ApiForpost
from beamable_python_sdk.paths.basic_realms_launch_message.delete import ApiFordelete


class BasicRealmsLaunchMessage(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
