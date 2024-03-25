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

from beamable_python_sdk.pydantic.rank_entry_columns import RankEntryColumns
from beamable_python_sdk.pydantic.rank_entry_stat import RankEntryStat

class RankEntry(BaseModel):
    rank: int = Field(alias='rank')

    gt: int = Field(alias='gt')

    stats: typing.Optional[typing.List[RankEntryStat]] = Field(None, alias='stats')

    score: typing.Optional[typing.Union[int, float]] = Field(None, alias='score')

    columns: typing.Optional[RankEntryColumns] = Field(None, alias='columns')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
