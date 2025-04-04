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


class TransferRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "recipientPlayer",
        }
        
        class properties:
            recipientPlayer = schemas.Int64Schema
            transaction = schemas.StrSchema
        
            @staticmethod
            def currencies() -> typing.Type['TransferRequestCurrencies']:
                return TransferRequestCurrencies
            __annotations__ = {
                "recipientPlayer": recipientPlayer,
                "transaction": transaction,
                "currencies": currencies,
            }
    
    recipientPlayer: MetaOapg.properties.recipientPlayer
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipientPlayer"]) -> MetaOapg.properties.recipientPlayer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction"]) -> MetaOapg.properties.transaction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencies"]) -> 'TransferRequestCurrencies': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["recipientPlayer", "transaction", "currencies", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipientPlayer"]) -> MetaOapg.properties.recipientPlayer: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction"]) -> typing.Union[MetaOapg.properties.transaction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencies"]) -> typing.Union['TransferRequestCurrencies', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["recipientPlayer", "transaction", "currencies", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        recipientPlayer: typing.Union[MetaOapg.properties.recipientPlayer, decimal.Decimal, int, ],
        transaction: typing.Union[MetaOapg.properties.transaction, str, schemas.Unset] = schemas.unset,
        currencies: typing.Union['TransferRequestCurrencies', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransferRequest':
        return super().__new__(
            cls,
            *args,
            recipientPlayer=recipientPlayer,
            transaction=transaction,
            currencies=currencies,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.transfer_request_currencies import TransferRequestCurrencies
