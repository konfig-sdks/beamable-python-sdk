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


class MatchMakingWindowResp(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "difficulty",
        }
        
        class properties:
            difficulty = schemas.IntSchema
            
            
            class matches(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MatchMakingRanking']:
                        return MatchMakingRanking
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MatchMakingRanking'], typing.List['MatchMakingRanking']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matches':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MatchMakingRanking':
                    return super().__getitem__(i)
            __annotations__ = {
                "difficulty": difficulty,
                "matches": matches,
            }
    
    difficulty: MetaOapg.properties.difficulty
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["difficulty"]) -> MetaOapg.properties.difficulty: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matches"]) -> MetaOapg.properties.matches: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["difficulty", "matches", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["difficulty"]) -> MetaOapg.properties.difficulty: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matches"]) -> typing.Union[MetaOapg.properties.matches, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["difficulty", "matches", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        difficulty: typing.Union[MetaOapg.properties.difficulty, decimal.Decimal, int, ],
        matches: typing.Union[MetaOapg.properties.matches, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MatchMakingWindowResp':
        return super().__new__(
            cls,
            *args,
            difficulty=difficulty,
            matches=matches,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.match_making_ranking import MatchMakingRanking
