from beamable_python_sdk.paths.basic_legacy_cloud_campaigns.get import ApiForget
from beamable_python_sdk.paths.basic_legacy_cloud_campaigns.post import ApiForpost
from beamable_python_sdk.paths.basic_legacy_cloud_campaigns.delete import ApiFordelete


class BasicLegacyCloudCampaigns(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
