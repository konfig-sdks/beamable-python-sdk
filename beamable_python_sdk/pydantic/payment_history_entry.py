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


class PaymentHistoryEntry(BaseModel):
    m_a_x__f_i_e_l_d__s_i_z_e: int = Field(alias='MAX_FIELD_SIZE')

    change: typing.Optional[str] = Field(None, alias='change')

    data: typing.Optional[str] = Field(None, alias='data')

    timestamp: typing.Optional[str] = Field(None, alias='timestamp')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
