from beamable_python_sdk.paths.basic_legacy_pvp_defs.get import ApiForget
from beamable_python_sdk.paths.basic_legacy_pvp_defs.put import ApiForput
from beamable_python_sdk.paths.basic_legacy_pvp_defs.delete import ApiFordelete


class BasicLegacyPvpDefs(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
