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

from beamable_python_sdk.pydantic.cloud_storage import CloudStorage
from beamable_python_sdk.pydantic.custom_cohort_rule import CustomCohortRule

class Cohort(BaseModel):
    assigned: int = Field(alias='assigned')

    name: typing.Optional[str] = Field(None, alias='name')

    custom_rule: typing.Optional[typing.List[CustomCohortRule]] = Field(None, alias='customRule')

    population_cap: typing.Optional[int] = Field(None, alias='populationCap')

    pct: typing.Optional[int] = Field(None, alias='pct')

    cloud_data: typing.Optional[typing.List[CloudStorage]] = Field(None, alias='cloudData')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
