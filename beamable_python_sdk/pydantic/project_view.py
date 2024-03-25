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

from beamable_python_sdk.pydantic.project_view_children import ProjectViewChildren

class ProjectView(BaseModel):
    project_name: str = Field(alias='projectName')

    pid: str = Field(alias='pid')

    secret: typing.Optional[str] = Field(None, alias='secret')

    parent: typing.Optional[str] = Field(None, alias='parent')

    children: typing.Optional[ProjectViewChildren] = Field(None, alias='children')

    archived: typing.Optional[bool] = Field(None, alias='archived')

    cid: typing.Optional[int] = Field(None, alias='cid')

    sharded: typing.Optional[bool] = Field(None, alias='sharded')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
