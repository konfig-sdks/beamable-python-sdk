# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from beamable_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from beamable_python_sdk.api_response import AsyncGeneratorResponse
from beamable_python_sdk import api_client, exceptions
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

from beamable_python_sdk.model.inventory_update_request_currency_properties import InventoryUpdateRequestCurrencyProperties as InventoryUpdateRequestCurrencyPropertiesSchema
from beamable_python_sdk.model.item_delete_request import ItemDeleteRequest as ItemDeleteRequestSchema
from beamable_python_sdk.model.inventory_update_request import InventoryUpdateRequest as InventoryUpdateRequestSchema
from beamable_python_sdk.model.item_create_request import ItemCreateRequest as ItemCreateRequestSchema
from beamable_python_sdk.model.inventory_update_request_item_content_ids import InventoryUpdateRequestItemContentIds as InventoryUpdateRequestItemContentIdsSchema
from beamable_python_sdk.model.preview_vip_bonus_response import PreviewVipBonusResponse as PreviewVipBonusResponseSchema
from beamable_python_sdk.model.item_update_request import ItemUpdateRequest as ItemUpdateRequestSchema
from beamable_python_sdk.model.inventory_update_request_currency_content_ids import InventoryUpdateRequestCurrencyContentIds as InventoryUpdateRequestCurrencyContentIdsSchema
from beamable_python_sdk.model.inventory_update_request_currencies import InventoryUpdateRequestCurrencies as InventoryUpdateRequestCurrenciesSchema

from beamable_python_sdk.type.preview_vip_bonus_response import PreviewVipBonusResponse
from beamable_python_sdk.type.inventory_update_request_currency_properties import InventoryUpdateRequestCurrencyProperties
from beamable_python_sdk.type.inventory_update_request import InventoryUpdateRequest
from beamable_python_sdk.type.item_delete_request import ItemDeleteRequest
from beamable_python_sdk.type.item_update_request import ItemUpdateRequest
from beamable_python_sdk.type.item_create_request import ItemCreateRequest
from beamable_python_sdk.type.inventory_update_request_currency_content_ids import InventoryUpdateRequestCurrencyContentIds
from beamable_python_sdk.type.inventory_update_request_item_content_ids import InventoryUpdateRequestItemContentIds
from beamable_python_sdk.type.inventory_update_request_currencies import InventoryUpdateRequestCurrencies

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.item_update_request import ItemUpdateRequest as ItemUpdateRequestPydantic
from beamable_python_sdk.pydantic.preview_vip_bonus_response import PreviewVipBonusResponse as PreviewVipBonusResponsePydantic
from beamable_python_sdk.pydantic.item_delete_request import ItemDeleteRequest as ItemDeleteRequestPydantic
from beamable_python_sdk.pydantic.inventory_update_request_item_content_ids import InventoryUpdateRequestItemContentIds as InventoryUpdateRequestItemContentIdsPydantic
from beamable_python_sdk.pydantic.item_create_request import ItemCreateRequest as ItemCreateRequestPydantic
from beamable_python_sdk.pydantic.inventory_update_request import InventoryUpdateRequest as InventoryUpdateRequestPydantic
from beamable_python_sdk.pydantic.inventory_update_request_currency_properties import InventoryUpdateRequestCurrencyProperties as InventoryUpdateRequestCurrencyPropertiesPydantic
from beamable_python_sdk.pydantic.inventory_update_request_currencies import InventoryUpdateRequestCurrencies as InventoryUpdateRequestCurrenciesPydantic
from beamable_python_sdk.pydantic.inventory_update_request_currency_content_ids import InventoryUpdateRequestCurrencyContentIds as InventoryUpdateRequestCurrencyContentIdsPydantic

from . import path

# Path params
ObjectIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'objectId': typing.Union[ObjectIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_object_id = api_client.PathParameter(
    name="objectId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ObjectIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = InventoryUpdateRequestSchema


request_body_inventory_update_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'scope',
]
SchemaFor200ResponseBodyApplicationJson = PreviewVipBonusResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PreviewVipBonusResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PreviewVipBonusResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_inventory_preview_mapped_args(
        self,
        empty: bool,
        currency_content_ids: InventoryUpdateRequestCurrencyContentIds,
        item_content_ids: InventoryUpdateRequestItemContentIds,
        object_id: str,
        currencies: typing.Optional[InventoryUpdateRequestCurrencies] = None,
        currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = None,
        apply_vip_bonus: typing.Optional[bool] = None,
        update_items: typing.Optional[typing.List[ItemUpdateRequest]] = None,
        new_items: typing.Optional[typing.List[ItemCreateRequest]] = None,
        transaction: typing.Optional[str] = None,
        delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if currencies is not None:
            _body["currencies"] = currencies
        if empty is not None:
            _body["empty"] = empty
        if currency_properties is not None:
            _body["currencyProperties"] = currency_properties
        if currency_content_ids is not None:
            _body["currencyContentIds"] = currency_content_ids
        if apply_vip_bonus is not None:
            _body["applyVipBonus"] = apply_vip_bonus
        if item_content_ids is not None:
            _body["itemContentIds"] = item_content_ids
        if update_items is not None:
            _body["updateItems"] = update_items
        if new_items is not None:
            _body["newItems"] = new_items
        if transaction is not None:
            _body["transaction"] = transaction
        if delete_items is not None:
            _body["deleteItems"] = delete_items
        args.body = _body
        if object_id is not None:
            _path_params["objectId"] = object_id
        args.path = _path_params
        return args

    async def _aupdate_inventory_preview_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_object_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/object/inventory/{objectId}/preview',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_inventory_update_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_inventory_preview_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_object_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/object/inventory/{objectId}/preview',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_inventory_update_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateInventoryPreviewRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_inventory_preview(
        self,
        empty: bool,
        currency_content_ids: InventoryUpdateRequestCurrencyContentIds,
        item_content_ids: InventoryUpdateRequestItemContentIds,
        object_id: str,
        currencies: typing.Optional[InventoryUpdateRequestCurrencies] = None,
        currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = None,
        apply_vip_bonus: typing.Optional[bool] = None,
        update_items: typing.Optional[typing.List[ItemUpdateRequest]] = None,
        new_items: typing.Optional[typing.List[ItemCreateRequest]] = None,
        transaction: typing.Optional[str] = None,
        delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_inventory_preview_mapped_args(
            empty=empty,
            currency_content_ids=currency_content_ids,
            item_content_ids=item_content_ids,
            object_id=object_id,
            currencies=currencies,
            currency_properties=currency_properties,
            apply_vip_bonus=apply_vip_bonus,
            update_items=update_items,
            new_items=new_items,
            transaction=transaction,
            delete_items=delete_items,
        )
        return await self._aupdate_inventory_preview_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_inventory_preview(
        self,
        empty: bool,
        currency_content_ids: InventoryUpdateRequestCurrencyContentIds,
        item_content_ids: InventoryUpdateRequestItemContentIds,
        object_id: str,
        currencies: typing.Optional[InventoryUpdateRequestCurrencies] = None,
        currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = None,
        apply_vip_bonus: typing.Optional[bool] = None,
        update_items: typing.Optional[typing.List[ItemUpdateRequest]] = None,
        new_items: typing.Optional[typing.List[ItemCreateRequest]] = None,
        transaction: typing.Optional[str] = None,
        delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_inventory_preview_mapped_args(
            empty=empty,
            currency_content_ids=currency_content_ids,
            item_content_ids=item_content_ids,
            object_id=object_id,
            currencies=currencies,
            currency_properties=currency_properties,
            apply_vip_bonus=apply_vip_bonus,
            update_items=update_items,
            new_items=new_items,
            transaction=transaction,
            delete_items=delete_items,
        )
        return self._update_inventory_preview_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateInventoryPreview(BaseApi):

    async def aupdate_inventory_preview(
        self,
        empty: bool,
        currency_content_ids: InventoryUpdateRequestCurrencyContentIds,
        item_content_ids: InventoryUpdateRequestItemContentIds,
        object_id: str,
        currencies: typing.Optional[InventoryUpdateRequestCurrencies] = None,
        currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = None,
        apply_vip_bonus: typing.Optional[bool] = None,
        update_items: typing.Optional[typing.List[ItemUpdateRequest]] = None,
        new_items: typing.Optional[typing.List[ItemCreateRequest]] = None,
        transaction: typing.Optional[str] = None,
        delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PreviewVipBonusResponsePydantic:
        raw_response = await self.raw.aupdate_inventory_preview(
            empty=empty,
            currency_content_ids=currency_content_ids,
            item_content_ids=item_content_ids,
            object_id=object_id,
            currencies=currencies,
            currency_properties=currency_properties,
            apply_vip_bonus=apply_vip_bonus,
            update_items=update_items,
            new_items=new_items,
            transaction=transaction,
            delete_items=delete_items,
            **kwargs,
        )
        if validate:
            return PreviewVipBonusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PreviewVipBonusResponsePydantic, raw_response.body)
    
    
    def update_inventory_preview(
        self,
        empty: bool,
        currency_content_ids: InventoryUpdateRequestCurrencyContentIds,
        item_content_ids: InventoryUpdateRequestItemContentIds,
        object_id: str,
        currencies: typing.Optional[InventoryUpdateRequestCurrencies] = None,
        currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = None,
        apply_vip_bonus: typing.Optional[bool] = None,
        update_items: typing.Optional[typing.List[ItemUpdateRequest]] = None,
        new_items: typing.Optional[typing.List[ItemCreateRequest]] = None,
        transaction: typing.Optional[str] = None,
        delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = None,
        validate: bool = False,
    ) -> PreviewVipBonusResponsePydantic:
        raw_response = self.raw.update_inventory_preview(
            empty=empty,
            currency_content_ids=currency_content_ids,
            item_content_ids=item_content_ids,
            object_id=object_id,
            currencies=currencies,
            currency_properties=currency_properties,
            apply_vip_bonus=apply_vip_bonus,
            update_items=update_items,
            new_items=new_items,
            transaction=transaction,
            delete_items=delete_items,
        )
        if validate:
            return PreviewVipBonusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PreviewVipBonusResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        empty: bool,
        currency_content_ids: InventoryUpdateRequestCurrencyContentIds,
        item_content_ids: InventoryUpdateRequestItemContentIds,
        object_id: str,
        currencies: typing.Optional[InventoryUpdateRequestCurrencies] = None,
        currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = None,
        apply_vip_bonus: typing.Optional[bool] = None,
        update_items: typing.Optional[typing.List[ItemUpdateRequest]] = None,
        new_items: typing.Optional[typing.List[ItemCreateRequest]] = None,
        transaction: typing.Optional[str] = None,
        delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_inventory_preview_mapped_args(
            empty=empty,
            currency_content_ids=currency_content_ids,
            item_content_ids=item_content_ids,
            object_id=object_id,
            currencies=currencies,
            currency_properties=currency_properties,
            apply_vip_bonus=apply_vip_bonus,
            update_items=update_items,
            new_items=new_items,
            transaction=transaction,
            delete_items=delete_items,
        )
        return await self._aupdate_inventory_preview_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        empty: bool,
        currency_content_ids: InventoryUpdateRequestCurrencyContentIds,
        item_content_ids: InventoryUpdateRequestItemContentIds,
        object_id: str,
        currencies: typing.Optional[InventoryUpdateRequestCurrencies] = None,
        currency_properties: typing.Optional[InventoryUpdateRequestCurrencyProperties] = None,
        apply_vip_bonus: typing.Optional[bool] = None,
        update_items: typing.Optional[typing.List[ItemUpdateRequest]] = None,
        new_items: typing.Optional[typing.List[ItemCreateRequest]] = None,
        transaction: typing.Optional[str] = None,
        delete_items: typing.Optional[typing.List[ItemDeleteRequest]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_inventory_preview_mapped_args(
            empty=empty,
            currency_content_ids=currency_content_ids,
            item_content_ids=item_content_ids,
            object_id=object_id,
            currencies=currencies,
            currency_properties=currency_properties,
            apply_vip_bonus=apply_vip_bonus,
            update_items=update_items,
            new_items=new_items,
            transaction=transaction,
            delete_items=delete_items,
        )
        return self._update_inventory_preview_oapg(
            body=args.body,
            path_params=args.path,
        )

