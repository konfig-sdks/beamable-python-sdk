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

from beamable_python_sdk.pydantic.promote_realm_request_content_manifest_ids import PromoteRealmRequestContentManifestIds
from beamable_python_sdk.pydantic.promote_realm_request_promotions import PromoteRealmRequestPromotions

class PromoteRealmRequest(BaseModel):
    source_pid: str = Field(alias='sourcePid')

    promotions: typing.Optional[PromoteRealmRequestPromotions] = Field(None, alias='promotions')

    content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = Field(None, alias='contentManifestIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
