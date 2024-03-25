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

from beamable_python_sdk.type.cloud_storage import CloudStorage
from beamable_python_sdk.type.custom_cohort_rule import CustomCohortRule

class RequiredCohort(TypedDict):
    assigned: int

class OptionalCohort(TypedDict, total=False):
    name: str

    customRule: typing.List[CustomCohortRule]

    populationCap: int

    pct: int

    cloudData: typing.List[CloudStorage]

class Cohort(RequiredCohort, OptionalCohort):
    pass
