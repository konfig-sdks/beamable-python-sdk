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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from beamable_python_sdk.pydantic.entitlement_definition_group_symbols import EntitlementDefinitionGroupSymbols
from beamable_python_sdk.pydantic.state_change_trigger import StateChangeTrigger

class EntitlementDefinition(BaseModel):
    max_grants: int = Field(alias='maxGrants')

    transferable: bool = Field(alias='transferable')

    revoke_mode: int = Field(alias='revokeMode')

    created: int = Field(alias='created')

    description: typing.Optional[str] = Field(None, alias='description')

    group_symbols: typing.Optional[EntitlementDefinitionGroupSymbols] = Field(None, alias='groupSymbols')

    name: typing.Optional[str] = Field(None, alias='name')

    claim_trigger: typing.Optional[StateChangeTrigger] = Field(None, alias='claimTrigger')

    image: typing.Optional[str] = Field(None, alias='image')

    grant_trigger: typing.Optional[StateChangeTrigger] = Field(None, alias='grantTrigger')

    terminal_expiration_secs: typing.Optional[int] = Field(None, alias='terminalExpirationSecs')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    replaces: typing.Optional[str] = Field(None, alias='replaces')

    parameterized: typing.Optional[bool] = Field(None, alias='parameterized')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
