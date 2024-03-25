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

from beamable_python_sdk.model.promote_realm_request_promotions import PromoteRealmRequestPromotions as PromoteRealmRequestPromotionsSchema
from beamable_python_sdk.model.promote_realm_response_old import PromoteRealmResponseOld as PromoteRealmResponseOldSchema
from beamable_python_sdk.model.promote_realm_request import PromoteRealmRequest as PromoteRealmRequestSchema
from beamable_python_sdk.model.promote_realm_request_content_manifest_ids import PromoteRealmRequestContentManifestIds as PromoteRealmRequestContentManifestIdsSchema

from beamable_python_sdk.type.promote_realm_request import PromoteRealmRequest
from beamable_python_sdk.type.promote_realm_request_content_manifest_ids import PromoteRealmRequestContentManifestIds
from beamable_python_sdk.type.promote_realm_response_old import PromoteRealmResponseOld
from beamable_python_sdk.type.promote_realm_request_promotions import PromoteRealmRequestPromotions

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.promote_realm_request import PromoteRealmRequest as PromoteRealmRequestPydantic
from beamable_python_sdk.pydantic.promote_realm_response_old import PromoteRealmResponseOld as PromoteRealmResponseOldPydantic
from beamable_python_sdk.pydantic.promote_realm_request_content_manifest_ids import PromoteRealmRequestContentManifestIds as PromoteRealmRequestContentManifestIdsPydantic
from beamable_python_sdk.pydantic.promote_realm_request_promotions import PromoteRealmRequestPromotions as PromoteRealmRequestPromotionsPydantic

# body param
SchemaForRequestBodyApplicationJson = PromoteRealmRequestSchema


request_body_promote_realm_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = PromoteRealmResponseOldSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PromoteRealmResponseOld


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PromoteRealmResponseOld


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

    def _project_promote_mapped_args(
        self,
        source_pid: str,
        promotions: typing.Optional[PromoteRealmRequestPromotions] = None,
        content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if source_pid is not None:
            _body["sourcePid"] = source_pid
        if promotions is not None:
            _body["promotions"] = promotions
        if content_manifest_ids is not None:
            _body["contentManifestIds"] = content_manifest_ids
        args.body = _body
        return args

    async def _aproject_promote_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/basic/realms/project/promote',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_promote_realm_request.serialize(body, content_type)
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


    def _project_promote_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/basic/realms/project/promote',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_promote_realm_request.serialize(body, content_type)
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


class ProjectPromoteRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aproject_promote(
        self,
        source_pid: str,
        promotions: typing.Optional[PromoteRealmRequestPromotions] = None,
        content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._project_promote_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return await self._aproject_promote_oapg(
            body=args.body,
            **kwargs,
        )
    
    def project_promote(
        self,
        source_pid: str,
        promotions: typing.Optional[PromoteRealmRequestPromotions] = None,
        content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._project_promote_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return self._project_promote_oapg(
            body=args.body,
        )

class ProjectPromote(BaseApi):

    async def aproject_promote(
        self,
        source_pid: str,
        promotions: typing.Optional[PromoteRealmRequestPromotions] = None,
        content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = None,
        validate: bool = False,
        **kwargs,
    ) -> PromoteRealmResponseOldPydantic:
        raw_response = await self.raw.aproject_promote(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
            **kwargs,
        )
        if validate:
            return PromoteRealmResponseOldPydantic(**raw_response.body)
        return api_client.construct_model_instance(PromoteRealmResponseOldPydantic, raw_response.body)
    
    
    def project_promote(
        self,
        source_pid: str,
        promotions: typing.Optional[PromoteRealmRequestPromotions] = None,
        content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = None,
        validate: bool = False,
    ) -> PromoteRealmResponseOldPydantic:
        raw_response = self.raw.project_promote(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        if validate:
            return PromoteRealmResponseOldPydantic(**raw_response.body)
        return api_client.construct_model_instance(PromoteRealmResponseOldPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        source_pid: str,
        promotions: typing.Optional[PromoteRealmRequestPromotions] = None,
        content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._project_promote_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return await self._aproject_promote_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        source_pid: str,
        promotions: typing.Optional[PromoteRealmRequestPromotions] = None,
        content_manifest_ids: typing.Optional[PromoteRealmRequestContentManifestIds] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._project_promote_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return self._project_promote_oapg(
            body=args.body,
        )

