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


class GroupScoreBinding(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "score",
        }
        
        class properties:
            score = schemas.IntSchema
            board = schemas.StrSchema
        
            @staticmethod
            def derivatives() -> typing.Type['GroupScoreBindingDerivatives']:
                return GroupScoreBindingDerivatives
            __annotations__ = {
                "score": score,
                "board": board,
                "derivatives": derivatives,
            }
    
    score: MetaOapg.properties.score
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["board"]) -> MetaOapg.properties.board: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["derivatives"]) -> 'GroupScoreBindingDerivatives': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["score", "board", "derivatives", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["board"]) -> typing.Union[MetaOapg.properties.board, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["derivatives"]) -> typing.Union['GroupScoreBindingDerivatives', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["score", "board", "derivatives", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, ],
        board: typing.Union[MetaOapg.properties.board, str, schemas.Unset] = schemas.unset,
        derivatives: typing.Union['GroupScoreBindingDerivatives', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupScoreBinding':
        return super().__new__(
            cls,
            *args,
            score=score,
            board=board,
            derivatives=derivatives,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.group_score_binding_derivatives import GroupScoreBindingDerivatives
