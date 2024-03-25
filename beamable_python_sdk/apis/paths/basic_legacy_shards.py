from beamable_python_sdk.paths.basic_legacy_shards.get import ApiForget
from beamable_python_sdk.paths.basic_legacy_shards.put import ApiForput
from beamable_python_sdk.paths.basic_legacy_shards.post import ApiForpost
from beamable_python_sdk.paths.basic_legacy_shards.delete import ApiFordelete


class BasicLegacyShards(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
