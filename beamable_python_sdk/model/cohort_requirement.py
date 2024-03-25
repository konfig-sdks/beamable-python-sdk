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


class CohortRequirement(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            trial = schemas.StrSchema
            cohort = schemas.StrSchema
            constraint = schemas.StrSchema
            __annotations__ = {
                "trial": trial,
                "cohort": cohort,
                "constraint": constraint,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trial"]) -> MetaOapg.properties.trial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cohort"]) -> MetaOapg.properties.cohort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["constraint"]) -> MetaOapg.properties.constraint: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["trial", "cohort", "constraint", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trial"]) -> typing.Union[MetaOapg.properties.trial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cohort"]) -> typing.Union[MetaOapg.properties.cohort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["constraint"]) -> typing.Union[MetaOapg.properties.constraint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["trial", "cohort", "constraint", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        trial: typing.Union[MetaOapg.properties.trial, str, schemas.Unset] = schemas.unset,
        cohort: typing.Union[MetaOapg.properties.cohort, str, schemas.Unset] = schemas.unset,
        constraint: typing.Union[MetaOapg.properties.constraint, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CohortRequirement':
        return super().__new__(
            cls,
            *args,
            trial=trial,
            cohort=cohort,
            constraint=constraint,
            _configuration=_configuration,
            **kwargs,
        )
