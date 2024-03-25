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

from beamable_python_sdk.pydantic.entitlement_def_request_group_symbols import EntitlementDefRequestGroupSymbols
from beamable_python_sdk.pydantic.state_change_trigger_def import StateChangeTriggerDef

class EntitlementDefRequest(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    max_grants: typing.Optional[int] = Field(None, alias='maxGrants')

    group_symbols: typing.Optional[EntitlementDefRequestGroupSymbols] = Field(None, alias='groupSymbols')

    transferable: typing.Optional[bool] = Field(None, alias='transferable')

    name: typing.Optional[str] = Field(None, alias='name')

    claim_trigger: typing.Optional[StateChangeTriggerDef] = Field(None, alias='claimTrigger')

    image: typing.Optional[str] = Field(None, alias='image')

    grant_trigger: typing.Optional[StateChangeTriggerDef] = Field(None, alias='grantTrigger')

    terminal_expiration_secs: typing.Optional[int] = Field(None, alias='terminalExpirationSecs')

    revoke_mode: typing.Optional[int] = Field(None, alias='revokeMode')

    replaces: typing.Optional[str] = Field(None, alias='replaces')

    parameterized: typing.Optional[bool] = Field(None, alias='parameterized')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
