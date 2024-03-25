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

from beamable_python_sdk.pydantic.match_making_ranking_variables import MatchMakingRankingVariables

class MatchMakingRanking(BaseModel):
    gt: int = Field(alias='gt')

    rank: int = Field(alias='rank')

    is_unranked: bool = Field(alias='isUnranked')

    variables: typing.Optional[MatchMakingRankingVariables] = Field(None, alias='variables')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
