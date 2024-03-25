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

from beamable_python_sdk.type.data_domain_memcached_hosts import DataDomainMemcachedHosts
from beamable_python_sdk.type.data_domain_message_bus_analytics import DataDomainMessageBusAnalytics
from beamable_python_sdk.type.data_domain_message_bus_common import DataDomainMessageBusCommon
from beamable_python_sdk.type.data_domain_mongo_hosts import DataDomainMongoHosts
from beamable_python_sdk.type.redis_shard import RedisShard

class RequiredDataDomain(TypedDict):
    memcachedHosts: DataDomainMemcachedHosts

    mongoSharded: bool

    mongoHosts: DataDomainMongoHosts

    mongoSSLEnabled: bool

class OptionalDataDomain(TypedDict, total=False):
    messageBusAnalytics: DataDomainMessageBusAnalytics

    mongoSSL: bool

    messageBusCommon: DataDomainMessageBusCommon

    redisShards: typing.List[RedisShard]

class DataDomain(RequiredDataDomain, OptionalDataDomain):
    pass
