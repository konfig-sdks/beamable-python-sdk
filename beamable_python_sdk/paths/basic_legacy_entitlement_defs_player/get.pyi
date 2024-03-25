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

from beamable_python_sdk.model.entitlement_list_response import EntitlementListResponse as EntitlementListResponseSchema

from beamable_python_sdk.type.entitlement_list_response import EntitlementListResponse

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.entitlement_list_response import EntitlementListResponse as EntitlementListResponsePydantic

# Query params
StateSchema = schemas.StrSchema
SkipSchema = schemas.IntSchema
SymbolSchema = schemas.StrSchema
IcwSchema = schemas.BoolSchema
SpecSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
GtSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'gt': typing.Union[GtSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'state': typing.Union[StateSchema, str, ],
        'skip': typing.Union[SkipSchema, decimal.Decimal, int, ],
        'symbol': typing.Union[SymbolSchema, str, ],
        'icw': typing.Union[IcwSchema, bool, ],
        'spec': typing.Union[SpecSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_state = api_client.QueryParameter(
    name="state",
    style=api_client.ParameterStyle.FORM,
    schema=StateSchema,
    explode=True,
)
request_query_skip = api_client.QueryParameter(
    name="skip",
    style=api_client.ParameterStyle.FORM,
    schema=SkipSchema,
    explode=True,
)
request_query_symbol = api_client.QueryParameter(
    name="symbol",
    style=api_client.ParameterStyle.FORM,
    schema=SymbolSchema,
    explode=True,
)
request_query_icw = api_client.QueryParameter(
    name="icw",
    style=api_client.ParameterStyle.FORM,
    schema=IcwSchema,
    explode=True,
)
request_query_spec = api_client.QueryParameter(
    name="spec",
    style=api_client.ParameterStyle.FORM,
    schema=SpecSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_gt = api_client.QueryParameter(
    name="gt",
    style=api_client.ParameterStyle.FORM,
    schema=GtSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = EntitlementListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EntitlementListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EntitlementListResponse


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_player_entitlements_mapped_args(
        self,
        gt: int,
        state: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        icw: typing.Optional[bool] = None,
        spec: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if state is not None:
            _query_params["state"] = state
        if skip is not None:
            _query_params["skip"] = skip
        if symbol is not None:
            _query_params["symbol"] = symbol
        if icw is not None:
            _query_params["icw"] = icw
        if spec is not None:
            _query_params["spec"] = spec
        if limit is not None:
            _query_params["limit"] = limit
        if gt is not None:
            _query_params["gt"] = gt
        args.query = _query_params
        return args

    async def _aget_player_entitlements_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_state,
            request_query_skip,
            request_query_symbol,
            request_query_icw,
            request_query_spec,
            request_query_limit,
            request_query_gt,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/basic/legacy-entitlement-defs/player',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_player_entitlements_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_state,
            request_query_skip,
            request_query_symbol,
            request_query_icw,
            request_query_spec,
            request_query_limit,
            request_query_gt,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/basic/legacy-entitlement-defs/player',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetPlayerEntitlementsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_player_entitlements(
        self,
        gt: int,
        state: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        icw: typing.Optional[bool] = None,
        spec: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_player_entitlements_mapped_args(
            gt=gt,
            state=state,
            skip=skip,
            symbol=symbol,
            icw=icw,
            spec=spec,
            limit=limit,
        )
        return await self._aget_player_entitlements_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_player_entitlements(
        self,
        gt: int,
        state: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        icw: typing.Optional[bool] = None,
        spec: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_player_entitlements_mapped_args(
            gt=gt,
            state=state,
            skip=skip,
            symbol=symbol,
            icw=icw,
            spec=spec,
            limit=limit,
        )
        return self._get_player_entitlements_oapg(
            query_params=args.query,
        )

class GetPlayerEntitlements(BaseApi):

    async def aget_player_entitlements(
        self,
        gt: int,
        state: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        icw: typing.Optional[bool] = None,
        spec: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> EntitlementListResponsePydantic:
        raw_response = await self.raw.aget_player_entitlements(
            gt=gt,
            state=state,
            skip=skip,
            symbol=symbol,
            icw=icw,
            spec=spec,
            limit=limit,
            **kwargs,
        )
        if validate:
            return EntitlementListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EntitlementListResponsePydantic, raw_response.body)
    
    
    def get_player_entitlements(
        self,
        gt: int,
        state: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        icw: typing.Optional[bool] = None,
        spec: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> EntitlementListResponsePydantic:
        raw_response = self.raw.get_player_entitlements(
            gt=gt,
            state=state,
            skip=skip,
            symbol=symbol,
            icw=icw,
            spec=spec,
            limit=limit,
        )
        if validate:
            return EntitlementListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EntitlementListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        gt: int,
        state: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        icw: typing.Optional[bool] = None,
        spec: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_player_entitlements_mapped_args(
            gt=gt,
            state=state,
            skip=skip,
            symbol=symbol,
            icw=icw,
            spec=spec,
            limit=limit,
        )
        return await self._aget_player_entitlements_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        gt: int,
        state: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        icw: typing.Optional[bool] = None,
        spec: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_player_entitlements_mapped_args(
            gt=gt,
            state=state,
            skip=skip,
            symbol=symbol,
            icw=icw,
            spec=spec,
            limit=limit,
        )
        return self._get_player_entitlements_oapg(
            query_params=args.query,
        )

