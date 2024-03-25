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


class PaymentAuditEntryViewModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "entitlements",
            "providerid",
            "txid",
            "details",
            "history",
            "gt",
            "providername",
            "txstate",
        }
        
        class properties:
            providerid = schemas.StrSchema
            
            
            class history(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PaymentHistoryEntryViewModel']:
                        return PaymentHistoryEntryViewModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PaymentHistoryEntryViewModel'], typing.List['PaymentHistoryEntryViewModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'history':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PaymentHistoryEntryViewModel':
                    return super().__getitem__(i)
            txid = schemas.Int64Schema
            providername = schemas.StrSchema
            txstate = schemas.StrSchema
            
            
            class entitlements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EntitlementGenerator']:
                        return EntitlementGenerator
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EntitlementGenerator'], typing.List['EntitlementGenerator']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entitlements':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EntitlementGenerator':
                    return super().__getitem__(i)
        
            @staticmethod
            def details() -> typing.Type['PaymentDetailsEntryViewModel']:
                return PaymentDetailsEntryViewModel
            gt = schemas.Int64Schema
            version = schemas.StrSchema
            
            
            class obtainItems(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ItemCreateRequest']:
                        return ItemCreateRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ItemCreateRequest'], typing.List['ItemCreateRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'obtainItems':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ItemCreateRequest':
                    return super().__getitem__(i)
            updated = schemas.Int64Schema
            
            
            class obtainCurrency(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CurrencyChange']:
                        return CurrencyChange
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CurrencyChange'], typing.List['CurrencyChange']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'obtainCurrency':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CurrencyChange':
                    return super().__getitem__(i)
            replayGuardValue = schemas.StrSchema
            created = schemas.Int64Schema
            __annotations__ = {
                "providerid": providerid,
                "history": history,
                "txid": txid,
                "providername": providername,
                "txstate": txstate,
                "entitlements": entitlements,
                "details": details,
                "gt": gt,
                "version": version,
                "obtainItems": obtainItems,
                "updated": updated,
                "obtainCurrency": obtainCurrency,
                "replayGuardValue": replayGuardValue,
                "created": created,
            }
    
    entitlements: MetaOapg.properties.entitlements
    providerid: MetaOapg.properties.providerid
    txid: MetaOapg.properties.txid
    details: 'PaymentDetailsEntryViewModel'
    history: MetaOapg.properties.history
    gt: MetaOapg.properties.gt
    providername: MetaOapg.properties.providername
    txstate: MetaOapg.properties.txstate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerid"]) -> MetaOapg.properties.providerid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["history"]) -> MetaOapg.properties.history: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txid"]) -> MetaOapg.properties.txid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providername"]) -> MetaOapg.properties.providername: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txstate"]) -> MetaOapg.properties.txstate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entitlements"]) -> MetaOapg.properties.entitlements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'PaymentDetailsEntryViewModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gt"]) -> MetaOapg.properties.gt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["obtainItems"]) -> MetaOapg.properties.obtainItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["obtainCurrency"]) -> MetaOapg.properties.obtainCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replayGuardValue"]) -> MetaOapg.properties.replayGuardValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["providerid", "history", "txid", "providername", "txstate", "entitlements", "details", "gt", "version", "obtainItems", "updated", "obtainCurrency", "replayGuardValue", "created", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerid"]) -> MetaOapg.properties.providerid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["history"]) -> MetaOapg.properties.history: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txid"]) -> MetaOapg.properties.txid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providername"]) -> MetaOapg.properties.providername: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txstate"]) -> MetaOapg.properties.txstate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entitlements"]) -> MetaOapg.properties.entitlements: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> 'PaymentDetailsEntryViewModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gt"]) -> MetaOapg.properties.gt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["obtainItems"]) -> typing.Union[MetaOapg.properties.obtainItems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> typing.Union[MetaOapg.properties.updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["obtainCurrency"]) -> typing.Union[MetaOapg.properties.obtainCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replayGuardValue"]) -> typing.Union[MetaOapg.properties.replayGuardValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["providerid", "history", "txid", "providername", "txstate", "entitlements", "details", "gt", "version", "obtainItems", "updated", "obtainCurrency", "replayGuardValue", "created", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        entitlements: typing.Union[MetaOapg.properties.entitlements, list, tuple, ],
        providerid: typing.Union[MetaOapg.properties.providerid, str, ],
        txid: typing.Union[MetaOapg.properties.txid, decimal.Decimal, int, ],
        details: 'PaymentDetailsEntryViewModel',
        history: typing.Union[MetaOapg.properties.history, list, tuple, ],
        gt: typing.Union[MetaOapg.properties.gt, decimal.Decimal, int, ],
        providername: typing.Union[MetaOapg.properties.providername, str, ],
        txstate: typing.Union[MetaOapg.properties.txstate, str, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        obtainItems: typing.Union[MetaOapg.properties.obtainItems, list, tuple, schemas.Unset] = schemas.unset,
        updated: typing.Union[MetaOapg.properties.updated, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        obtainCurrency: typing.Union[MetaOapg.properties.obtainCurrency, list, tuple, schemas.Unset] = schemas.unset,
        replayGuardValue: typing.Union[MetaOapg.properties.replayGuardValue, str, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentAuditEntryViewModel':
        return super().__new__(
            cls,
            *args,
            entitlements=entitlements,
            providerid=providerid,
            txid=txid,
            details=details,
            history=history,
            gt=gt,
            providername=providername,
            txstate=txstate,
            version=version,
            obtainItems=obtainItems,
            updated=updated,
            obtainCurrency=obtainCurrency,
            replayGuardValue=replayGuardValue,
            created=created,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.currency_change import CurrencyChange
from beamable_python_sdk.model.entitlement_generator import EntitlementGenerator
from beamable_python_sdk.model.item_create_request import ItemCreateRequest
from beamable_python_sdk.model.payment_details_entry_view_model import PaymentDetailsEntryViewModel
from beamable_python_sdk.model.payment_history_entry_view_model import PaymentHistoryEntryViewModel
