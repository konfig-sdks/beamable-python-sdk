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


class CustomCohortRule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            customAttr = schemas.StrSchema
            customOp = schemas.StrSchema
        
            @staticmethod
            def customVal() -> typing.Type['CustomCohortRuleCustomVal']:
                return CustomCohortRuleCustomVal
            __annotations__ = {
                "customAttr": customAttr,
                "customOp": customOp,
                "customVal": customVal,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customAttr"]) -> MetaOapg.properties.customAttr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customOp"]) -> MetaOapg.properties.customOp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customVal"]) -> 'CustomCohortRuleCustomVal': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customAttr", "customOp", "customVal", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customAttr"]) -> typing.Union[MetaOapg.properties.customAttr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customOp"]) -> typing.Union[MetaOapg.properties.customOp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customVal"]) -> typing.Union['CustomCohortRuleCustomVal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customAttr", "customOp", "customVal", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customAttr: typing.Union[MetaOapg.properties.customAttr, str, schemas.Unset] = schemas.unset,
        customOp: typing.Union[MetaOapg.properties.customOp, str, schemas.Unset] = schemas.unset,
        customVal: typing.Union['CustomCohortRuleCustomVal', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomCohortRule':
        return super().__new__(
            cls,
            *args,
            customAttr=customAttr,
            customOp=customOp,
            customVal=customVal,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.custom_cohort_rule_custom_val import CustomCohortRuleCustomVal
