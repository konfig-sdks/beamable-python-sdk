from beamable_python_sdk.paths.basic_legacy_cloud_templates.get import ApiForget
from beamable_python_sdk.paths.basic_legacy_cloud_templates.post import ApiForpost
from beamable_python_sdk.paths.basic_legacy_cloud_templates.delete import ApiFordelete


class BasicLegacyCloudTemplates(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
