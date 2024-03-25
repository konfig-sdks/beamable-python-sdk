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

from beamable_python_sdk.model.list_audit_response import ListAuditResponse as ListAuditResponseSchema

from beamable_python_sdk.type.list_audit_response import ListAuditResponse

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.list_audit_response import ListAuditResponse as ListAuditResponsePydantic

# Query params
ProvideridSchema = schemas.StrSchema
ProviderSchema = schemas.StrSchema
StateSchema = schemas.StrSchema
TxidSchema = schemas.IntSchema
PlayerSchema = schemas.IntSchema
StartSchema = schemas.IntSchema
LimitSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'providerid': typing.Union[ProvideridSchema, str, ],
        'provider': typing.Union[ProviderSchema, str, ],
        'state': typing.Union[StateSchema, str, ],
        'txid': typing.Union[TxidSchema, decimal.Decimal, int, ],
        'player': typing.Union[PlayerSchema, decimal.Decimal, int, ],
        'start': typing.Union[StartSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_providerid = api_client.QueryParameter(
    name="providerid",
    style=api_client.ParameterStyle.FORM,
    schema=ProvideridSchema,
    explode=True,
)
request_query_provider = api_client.QueryParameter(
    name="provider",
    style=api_client.ParameterStyle.FORM,
    schema=ProviderSchema,
    explode=True,
)
request_query_state = api_client.QueryParameter(
    name="state",
    style=api_client.ParameterStyle.FORM,
    schema=StateSchema,
    explode=True,
)
request_query_txid = api_client.QueryParameter(
    name="txid",
    style=api_client.ParameterStyle.FORM,
    schema=TxidSchema,
    explode=True,
)
request_query_player = api_client.QueryParameter(
    name="player",
    style=api_client.ParameterStyle.FORM,
    schema=PlayerSchema,
    explode=True,
)
request_query_start = api_client.QueryParameter(
    name="start",
    style=api_client.ParameterStyle.FORM,
    schema=StartSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ListAuditResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ListAuditResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ListAuditResponse


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

    def _get_payment_audits_mapped_args(
        self,
        providerid: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        txid: typing.Optional[int] = None,
        player: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if providerid is not None:
            _query_params["providerid"] = providerid
        if provider is not None:
            _query_params["provider"] = provider
        if state is not None:
            _query_params["state"] = state
        if txid is not None:
            _query_params["txid"] = txid
        if player is not None:
            _query_params["player"] = player
        if start is not None:
            _query_params["start"] = start
        if limit is not None:
            _query_params["limit"] = limit
        args.query = _query_params
        return args

    async def _aget_payment_audits_oapg(
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
            request_query_providerid,
            request_query_provider,
            request_query_state,
            request_query_txid,
            request_query_player,
            request_query_start,
            request_query_limit,
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
            path_template='/basic/payments/audits',
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


    def _get_payment_audits_oapg(
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
            request_query_providerid,
            request_query_provider,
            request_query_state,
            request_query_txid,
            request_query_player,
            request_query_start,
            request_query_limit,
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
            path_template='/basic/payments/audits',
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


class GetPaymentAuditsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_payment_audits(
        self,
        providerid: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        txid: typing.Optional[int] = None,
        player: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_payment_audits_mapped_args(
            providerid=providerid,
            provider=provider,
            state=state,
            txid=txid,
            player=player,
            start=start,
            limit=limit,
        )
        return await self._aget_payment_audits_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_payment_audits(
        self,
        providerid: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        txid: typing.Optional[int] = None,
        player: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_payment_audits_mapped_args(
            providerid=providerid,
            provider=provider,
            state=state,
            txid=txid,
            player=player,
            start=start,
            limit=limit,
        )
        return self._get_payment_audits_oapg(
            query_params=args.query,
        )

class GetPaymentAudits(BaseApi):

    async def aget_payment_audits(
        self,
        providerid: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        txid: typing.Optional[int] = None,
        player: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ListAuditResponsePydantic:
        raw_response = await self.raw.aget_payment_audits(
            providerid=providerid,
            provider=provider,
            state=state,
            txid=txid,
            player=player,
            start=start,
            limit=limit,
            **kwargs,
        )
        if validate:
            return ListAuditResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ListAuditResponsePydantic, raw_response.body)
    
    
    def get_payment_audits(
        self,
        providerid: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        txid: typing.Optional[int] = None,
        player: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ListAuditResponsePydantic:
        raw_response = self.raw.get_payment_audits(
            providerid=providerid,
            provider=provider,
            state=state,
            txid=txid,
            player=player,
            start=start,
            limit=limit,
        )
        if validate:
            return ListAuditResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ListAuditResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        providerid: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        txid: typing.Optional[int] = None,
        player: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_payment_audits_mapped_args(
            providerid=providerid,
            provider=provider,
            state=state,
            txid=txid,
            player=player,
            start=start,
            limit=limit,
        )
        return await self._aget_payment_audits_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        providerid: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        txid: typing.Optional[int] = None,
        player: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_payment_audits_mapped_args(
            providerid=providerid,
            provider=provider,
            state=state,
            txid=txid,
            player=player,
            start=start,
            limit=limit,
        )
        return self._get_payment_audits_oapg(
            query_params=args.query,
        )

