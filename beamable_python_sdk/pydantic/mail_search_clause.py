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

from beamable_python_sdk.pydantic.mail_search_clause_categories import MailSearchClauseCategories
from beamable_python_sdk.pydantic.mail_search_clause_states import MailSearchClauseStates

class MailSearchClause(BaseModel):
    only_count: bool = Field(alias='onlyCount')

    for_sender: typing.Optional[int] = Field(None, alias='forSender')

    name: typing.Optional[str] = Field(None, alias='name')

    categories: typing.Optional[MailSearchClauseCategories] = Field(None, alias='categories')

    start: typing.Optional[int] = Field(None, alias='start')

    limit: typing.Optional[int] = Field(None, alias='limit')

    states: typing.Optional[MailSearchClauseStates] = Field(None, alias='states')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
