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

from beamable_python_sdk.model.group_search_response import GroupSearchResponse as GroupSearchResponseSchema

from beamable_python_sdk.type.group_search_response import GroupSearchResponse

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.group_search_response import GroupSearchResponse as GroupSearchResponsePydantic

# Query params
NameSchema = schemas.StrSchema
ScoreMinSchema = schemas.IntSchema
SortFieldSchema = schemas.StrSchema
UserScoreSchema = schemas.IntSchema
HasSlotsSchema = schemas.BoolSchema
EnrollmentTypesSchema = schemas.StrSchema
OffsetSchema = schemas.IntSchema
ScoreMaxSchema = schemas.IntSchema
SubGroupSchema = schemas.BoolSchema
SortValueSchema = schemas.IntSchema
TypeSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'name': typing.Union[NameSchema, str, ],
        'scoreMin': typing.Union[ScoreMinSchema, decimal.Decimal, int, ],
        'sortField': typing.Union[SortFieldSchema, str, ],
        'userScore': typing.Union[UserScoreSchema, decimal.Decimal, int, ],
        'hasSlots': typing.Union[HasSlotsSchema, bool, ],
        'enrollmentTypes': typing.Union[EnrollmentTypesSchema, str, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'scoreMax': typing.Union[ScoreMaxSchema, decimal.Decimal, int, ],
        'subGroup': typing.Union[SubGroupSchema, bool, ],
        'sortValue': typing.Union[SortValueSchema, decimal.Decimal, int, ],
        'type': typing.Union[TypeSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    explode=True,
)
request_query_score_min = api_client.QueryParameter(
    name="scoreMin",
    style=api_client.ParameterStyle.FORM,
    schema=ScoreMinSchema,
    explode=True,
)
request_query_sort_field = api_client.QueryParameter(
    name="sortField",
    style=api_client.ParameterStyle.FORM,
    schema=SortFieldSchema,
    explode=True,
)
request_query_user_score = api_client.QueryParameter(
    name="userScore",
    style=api_client.ParameterStyle.FORM,
    schema=UserScoreSchema,
    explode=True,
)
request_query_has_slots = api_client.QueryParameter(
    name="hasSlots",
    style=api_client.ParameterStyle.FORM,
    schema=HasSlotsSchema,
    explode=True,
)
request_query_enrollment_types = api_client.QueryParameter(
    name="enrollmentTypes",
    style=api_client.ParameterStyle.FORM,
    schema=EnrollmentTypesSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_score_max = api_client.QueryParameter(
    name="scoreMax",
    style=api_client.ParameterStyle.FORM,
    schema=ScoreMaxSchema,
    explode=True,
)
request_query_sub_group = api_client.QueryParameter(
    name="subGroup",
    style=api_client.ParameterStyle.FORM,
    schema=SubGroupSchema,
    explode=True,
)
request_query_sort_value = api_client.QueryParameter(
    name="sortValue",
    style=api_client.ParameterStyle.FORM,
    schema=SortValueSchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
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
SchemaFor200ResponseBodyApplicationJson = GroupSearchResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GroupSearchResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GroupSearchResponse


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

    def _search_users_mapped_args(
        self,
        object_id: str,
        name: typing.Optional[str] = None,
        score_min: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        user_score: typing.Optional[int] = None,
        has_slots: typing.Optional[bool] = None,
        enrollment_types: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        score_max: typing.Optional[int] = None,
        sub_group: typing.Optional[bool] = None,
        sort_value: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if name is not None:
            _query_params["name"] = name
        if score_min is not None:
            _query_params["scoreMin"] = score_min
        if sort_field is not None:
            _query_params["sortField"] = sort_field
        if user_score is not None:
            _query_params["userScore"] = user_score
        if has_slots is not None:
            _query_params["hasSlots"] = has_slots
        if enrollment_types is not None:
            _query_params["enrollmentTypes"] = enrollment_types
        if offset is not None:
            _query_params["offset"] = offset
        if score_max is not None:
            _query_params["scoreMax"] = score_max
        if sub_group is not None:
            _query_params["subGroup"] = sub_group
        if sort_value is not None:
            _query_params["sortValue"] = sort_value
        if type is not None:
            _query_params["type"] = type
        if limit is not None:
            _query_params["limit"] = limit
        if object_id is not None:
            _path_params["objectId"] = object_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _asearch_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_name,
            request_query_score_min,
            request_query_sort_field,
            request_query_user_score,
            request_query_has_slots,
            request_query_enrollment_types,
            request_query_offset,
            request_query_score_max,
            request_query_sub_group,
            request_query_sort_value,
            request_query_type,
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
            path_template='/object/group-users/{objectId}/search',
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


    def _search_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_name,
            request_query_score_min,
            request_query_sort_field,
            request_query_user_score,
            request_query_has_slots,
            request_query_enrollment_types,
            request_query_offset,
            request_query_score_max,
            request_query_sub_group,
            request_query_sort_value,
            request_query_type,
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
            path_template='/object/group-users/{objectId}/search',
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


class SearchUsersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_users(
        self,
        object_id: str,
        name: typing.Optional[str] = None,
        score_min: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        user_score: typing.Optional[int] = None,
        has_slots: typing.Optional[bool] = None,
        enrollment_types: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        score_max: typing.Optional[int] = None,
        sub_group: typing.Optional[bool] = None,
        sort_value: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_users_mapped_args(
            object_id=object_id,
            name=name,
            score_min=score_min,
            sort_field=sort_field,
            user_score=user_score,
            has_slots=has_slots,
            enrollment_types=enrollment_types,
            offset=offset,
            score_max=score_max,
            sub_group=sub_group,
            sort_value=sort_value,
            type=type,
            limit=limit,
        )
        return await self._asearch_users_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def search_users(
        self,
        object_id: str,
        name: typing.Optional[str] = None,
        score_min: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        user_score: typing.Optional[int] = None,
        has_slots: typing.Optional[bool] = None,
        enrollment_types: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        score_max: typing.Optional[int] = None,
        sub_group: typing.Optional[bool] = None,
        sort_value: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_users_mapped_args(
            object_id=object_id,
            name=name,
            score_min=score_min,
            sort_field=sort_field,
            user_score=user_score,
            has_slots=has_slots,
            enrollment_types=enrollment_types,
            offset=offset,
            score_max=score_max,
            sub_group=sub_group,
            sort_value=sort_value,
            type=type,
            limit=limit,
        )
        return self._search_users_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class SearchUsers(BaseApi):

    async def asearch_users(
        self,
        object_id: str,
        name: typing.Optional[str] = None,
        score_min: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        user_score: typing.Optional[int] = None,
        has_slots: typing.Optional[bool] = None,
        enrollment_types: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        score_max: typing.Optional[int] = None,
        sub_group: typing.Optional[bool] = None,
        sort_value: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> GroupSearchResponsePydantic:
        raw_response = await self.raw.asearch_users(
            object_id=object_id,
            name=name,
            score_min=score_min,
            sort_field=sort_field,
            user_score=user_score,
            has_slots=has_slots,
            enrollment_types=enrollment_types,
            offset=offset,
            score_max=score_max,
            sub_group=sub_group,
            sort_value=sort_value,
            type=type,
            limit=limit,
            **kwargs,
        )
        if validate:
            return GroupSearchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GroupSearchResponsePydantic, raw_response.body)
    
    
    def search_users(
        self,
        object_id: str,
        name: typing.Optional[str] = None,
        score_min: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        user_score: typing.Optional[int] = None,
        has_slots: typing.Optional[bool] = None,
        enrollment_types: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        score_max: typing.Optional[int] = None,
        sub_group: typing.Optional[bool] = None,
        sort_value: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> GroupSearchResponsePydantic:
        raw_response = self.raw.search_users(
            object_id=object_id,
            name=name,
            score_min=score_min,
            sort_field=sort_field,
            user_score=user_score,
            has_slots=has_slots,
            enrollment_types=enrollment_types,
            offset=offset,
            score_max=score_max,
            sub_group=sub_group,
            sort_value=sort_value,
            type=type,
            limit=limit,
        )
        if validate:
            return GroupSearchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GroupSearchResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        object_id: str,
        name: typing.Optional[str] = None,
        score_min: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        user_score: typing.Optional[int] = None,
        has_slots: typing.Optional[bool] = None,
        enrollment_types: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        score_max: typing.Optional[int] = None,
        sub_group: typing.Optional[bool] = None,
        sort_value: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_users_mapped_args(
            object_id=object_id,
            name=name,
            score_min=score_min,
            sort_field=sort_field,
            user_score=user_score,
            has_slots=has_slots,
            enrollment_types=enrollment_types,
            offset=offset,
            score_max=score_max,
            sub_group=sub_group,
            sort_value=sort_value,
            type=type,
            limit=limit,
        )
        return await self._asearch_users_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        object_id: str,
        name: typing.Optional[str] = None,
        score_min: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        user_score: typing.Optional[int] = None,
        has_slots: typing.Optional[bool] = None,
        enrollment_types: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        score_max: typing.Optional[int] = None,
        sub_group: typing.Optional[bool] = None,
        sort_value: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_users_mapped_args(
            object_id=object_id,
            name=name,
            score_min=score_min,
            sort_field=sort_field,
            user_score=user_score,
            has_slots=has_slots,
            enrollment_types=enrollment_types,
            offset=offset,
            score_max=score_max,
            sub_group=sub_group,
            sort_value=sort_value,
            type=type,
            limit=limit,
        )
        return self._search_users_oapg(
            query_params=args.query,
            path_params=args.path,
        )

