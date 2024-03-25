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

from beamable_python_sdk.pydantic.data_domain_memcached_hosts import DataDomainMemcachedHosts
from beamable_python_sdk.pydantic.data_domain_message_bus_analytics import DataDomainMessageBusAnalytics
from beamable_python_sdk.pydantic.data_domain_message_bus_common import DataDomainMessageBusCommon
from beamable_python_sdk.pydantic.data_domain_mongo_hosts import DataDomainMongoHosts
from beamable_python_sdk.pydantic.redis_shard import RedisShard

class DataDomain(BaseModel):
    memcached_hosts: DataDomainMemcachedHosts = Field(alias='memcachedHosts')

    mongo_sharded: bool = Field(alias='mongoSharded')

    mongo_hosts: DataDomainMongoHosts = Field(alias='mongoHosts')

    mongo_s_s_l_enabled: bool = Field(alias='mongoSSLEnabled')

    message_bus_analytics: typing.Optional[DataDomainMessageBusAnalytics] = Field(None, alias='messageBusAnalytics')

    mongo_s_s_l: typing.Optional[bool] = Field(None, alias='mongoSSL')

    message_bus_common: typing.Optional[DataDomainMessageBusCommon] = Field(None, alias='messageBusCommon')

    redis_shards: typing.Optional[typing.List[RedisShard]] = Field(None, alias='redisShards')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
