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

from beamable_python_sdk.type.project_children import ProjectChildren
from beamable_python_sdk.type.project_config import ProjectConfig
from beamable_python_sdk.type.project_custom_charts import ProjectCustomCharts

class RequiredProject(TypedDict):
    secret: str

    name: str

    customCharts: ProjectCustomCharts

    root: bool

    archived: bool

    plan: str

class OptionalProject(TypedDict, total=False):
    displayName: str

    parent: str

    children: ProjectChildren

    config: ProjectConfig

    status: str

    sharded: bool

    sigval: bool

    created: int

class Project(RequiredProject, OptionalProject):
    pass
