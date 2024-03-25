from beamable_python_sdk.paths.basic_legacy_entitlement_defs.get import ApiForget
from beamable_python_sdk.paths.basic_legacy_entitlement_defs.put import ApiForput
from beamable_python_sdk.paths.basic_legacy_entitlement_defs.post import ApiForpost
from beamable_python_sdk.paths.basic_legacy_entitlement_defs.delete import ApiFordelete


class BasicLegacyEntitlementDefs(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
