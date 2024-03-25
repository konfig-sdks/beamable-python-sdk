# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from beamable_python_sdk import schemas  # noqa: F401


class Event(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            start_date = schemas.StrSchema
            
            
            class phases(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EventPhase']:
                        return EventPhase
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EventPhase'], typing.List['EventPhase']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phases':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EventPhase':
                    return super().__getitem__(i)
            partition_size = schemas.IntSchema
        
            @staticmethod
            def group_rewards() -> typing.Type['EventGroupRewards']:
                return EventGroupRewards
        
            @staticmethod
            def cohortSettings() -> typing.Type['LeaderboardCohortSettings']:
                return LeaderboardCohortSettings
        
            @staticmethod
            def permissions() -> typing.Type['ClientPermission']:
                return ClientPermission
        
            @staticmethod
            def stores() -> typing.Type['EventStores']:
                return EventStores
            symbol = schemas.StrSchema
            
            
            class score_rewards(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EventRewardItem']:
                        return EventRewardItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EventRewardItem'], typing.List['EventRewardItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'score_rewards':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EventRewardItem':
                    return super().__getitem__(i)
        
            @staticmethod
            def schedule() -> typing.Type['Schedule']:
                return Schedule
            
            
            class rank_rewards(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EventRewardItem']:
                        return EventRewardItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EventRewardItem'], typing.List['EventRewardItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rank_rewards':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EventRewardItem':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "start_date": start_date,
                "phases": phases,
                "partition_size": partition_size,
                "group_rewards": group_rewards,
                "cohortSettings": cohortSettings,
                "permissions": permissions,
                "stores": stores,
                "symbol": symbol,
                "score_rewards": score_rewards,
                "schedule": schedule,
                "rank_rewards": rank_rewards,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phases"]) -> MetaOapg.properties.phases: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partition_size"]) -> MetaOapg.properties.partition_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_rewards"]) -> 'EventGroupRewards': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cohortSettings"]) -> 'LeaderboardCohortSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'ClientPermission': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stores"]) -> 'EventStores': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score_rewards"]) -> MetaOapg.properties.score_rewards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'Schedule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rank_rewards"]) -> MetaOapg.properties.rank_rewards: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "start_date", "phases", "partition_size", "group_rewards", "cohortSettings", "permissions", "stores", "symbol", "score_rewards", "schedule", "rank_rewards", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phases"]) -> typing.Union[MetaOapg.properties.phases, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partition_size"]) -> typing.Union[MetaOapg.properties.partition_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_rewards"]) -> typing.Union['EventGroupRewards', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cohortSettings"]) -> typing.Union['LeaderboardCohortSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union['ClientPermission', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stores"]) -> typing.Union['EventStores', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> typing.Union[MetaOapg.properties.symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score_rewards"]) -> typing.Union[MetaOapg.properties.score_rewards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> typing.Union['Schedule', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rank_rewards"]) -> typing.Union[MetaOapg.properties.rank_rewards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "start_date", "phases", "partition_size", "group_rewards", "cohortSettings", "permissions", "stores", "symbol", "score_rewards", "schedule", "rank_rewards", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        phases: typing.Union[MetaOapg.properties.phases, list, tuple, schemas.Unset] = schemas.unset,
        partition_size: typing.Union[MetaOapg.properties.partition_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        group_rewards: typing.Union['EventGroupRewards', schemas.Unset] = schemas.unset,
        cohortSettings: typing.Union['LeaderboardCohortSettings', schemas.Unset] = schemas.unset,
        permissions: typing.Union['ClientPermission', schemas.Unset] = schemas.unset,
        stores: typing.Union['EventStores', schemas.Unset] = schemas.unset,
        symbol: typing.Union[MetaOapg.properties.symbol, str, schemas.Unset] = schemas.unset,
        score_rewards: typing.Union[MetaOapg.properties.score_rewards, list, tuple, schemas.Unset] = schemas.unset,
        schedule: typing.Union['Schedule', schemas.Unset] = schemas.unset,
        rank_rewards: typing.Union[MetaOapg.properties.rank_rewards, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Event':
        return super().__new__(
            cls,
            *args,
            name=name,
            start_date=start_date,
            phases=phases,
            partition_size=partition_size,
            group_rewards=group_rewards,
            cohortSettings=cohortSettings,
            permissions=permissions,
            stores=stores,
            symbol=symbol,
            score_rewards=score_rewards,
            schedule=schedule,
            rank_rewards=rank_rewards,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.client_permission import ClientPermission
from beamable_python_sdk.model.event_group_rewards import EventGroupRewards
from beamable_python_sdk.model.event_phase import EventPhase
from beamable_python_sdk.model.event_reward_item import EventRewardItem
from beamable_python_sdk.model.event_stores import EventStores
from beamable_python_sdk.model.leaderboard_cohort_settings import LeaderboardCohortSettings
from beamable_python_sdk.model.schedule import Schedule
