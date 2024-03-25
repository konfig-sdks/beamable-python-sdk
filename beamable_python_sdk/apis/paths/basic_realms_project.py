from beamable_python_sdk.paths.basic_realms_project.get import ApiForget
from beamable_python_sdk.paths.basic_realms_project.put import ApiForput
from beamable_python_sdk.paths.basic_realms_project.post import ApiForpost
from beamable_python_sdk.paths.basic_realms_project.delete import ApiFordelete


class BasicRealmsProject(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
