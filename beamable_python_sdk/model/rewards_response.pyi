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


class RewardsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class rewardCurrencies(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TournamentReward']:
                        return TournamentReward
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TournamentReward'], typing.List['TournamentReward']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rewardCurrencies':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TournamentReward':
                    return super().__getitem__(i)
            __annotations__ = {
                "rewardCurrencies": rewardCurrencies,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rewardCurrencies"]) -> MetaOapg.properties.rewardCurrencies: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rewardCurrencies", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rewardCurrencies"]) -> typing.Union[MetaOapg.properties.rewardCurrencies, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rewardCurrencies", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        rewardCurrencies: typing.Union[MetaOapg.properties.rewardCurrencies, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RewardsResponse':
        return super().__new__(
            cls,
            *args,
            rewardCurrencies=rewardCurrencies,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.tournament_reward import TournamentReward
