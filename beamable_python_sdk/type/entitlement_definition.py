# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from beamable_python_sdk.type.entitlement_definition_group_symbols import EntitlementDefinitionGroupSymbols
from beamable_python_sdk.type.state_change_trigger import StateChangeTrigger

class RequiredEntitlementDefinition(TypedDict):
    maxGrants: int

    transferable: bool

    revokeMode: int

    created: int

class OptionalEntitlementDefinition(TypedDict, total=False):
    description: str

    groupSymbols: EntitlementDefinitionGroupSymbols

    name: str

    claimTrigger: StateChangeTrigger

    image: str

    grantTrigger: StateChangeTrigger

    terminalExpirationSecs: int

    symbol: str

    replaces: str

    parameterized: bool

class EntitlementDefinition(RequiredEntitlementDefinition, OptionalEntitlementDefinition):
    pass
