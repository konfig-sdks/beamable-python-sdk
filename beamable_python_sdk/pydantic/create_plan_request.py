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

from beamable_python_sdk.pydantic.create_plan_request_message_bus_analytics import CreatePlanRequestMessageBusAnalytics
from beamable_python_sdk.pydantic.create_plan_request_message_bus_common import CreatePlanRequestMessageBusCommon
from beamable_python_sdk.pydantic.redis_shard_request import RedisShardRequest

class CreatePlanRequest(BaseModel):
    name: str = Field(alias='name')

    memcached_hosts: str = Field(alias='memcachedHosts')

    mongo_s_s_l: bool = Field(alias='mongoSSL')

    platform_j_b_d_c: str = Field(alias='platformJBDC')

    sharded: bool = Field(alias='sharded')

    mongo_hosts: str = Field(alias='mongoHosts')

    redis_shards: typing.List[RedisShardRequest] = Field(alias='redisShards')

    message_bus_analytics: typing.Optional[CreatePlanRequestMessageBusAnalytics] = Field(None, alias='messageBusAnalytics')

    message_bus_common: typing.Optional[CreatePlanRequestMessageBusCommon] = Field(None, alias='messageBusCommon')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
