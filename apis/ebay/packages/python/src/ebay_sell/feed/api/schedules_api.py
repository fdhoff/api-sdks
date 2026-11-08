# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.feed import models as _models
from ebay_sell.feed.models.create_user_schedule_request import CreateUserScheduleRequest
from ebay_sell.feed.models.schedule_template_collection import ScheduleTemplateCollection
from ebay_sell.feed.models.schedule_template_response import ScheduleTemplateResponse
from ebay_sell.feed.models.update_user_schedule_request import UpdateUserScheduleRequest
from ebay_sell.feed.models.user_schedule_collection import UserScheduleCollection
from ebay_sell.feed.models.user_schedule_response import UserScheduleResponse

_create_schedule: Operation[object] = Operation(
    id="createSchedule",
    method="POST",
    path="/sell/feed/v1/schedule",
    resource="schedules",
    name="create",
    params=(),
    response=object,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_delete_schedule: Operation[None] = Operation(
    id="deleteSchedule",
    method="DELETE",
    path="/sell/feed/v1/schedule/{schedule_id}",
    resource="schedules",
    name="delete",
    params=(Param("schedule_id", "schedule_id", "path"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_schedule: Operation[UserScheduleResponse] = Operation(
    id="getSchedule",
    method="GET",
    path="/sell/feed/v1/schedule/{schedule_id}",
    resource="schedules",
    name="get",
    params=(Param("schedule_id", "schedule_id", "path"),),
    response=UserScheduleResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_schedule_template: Operation[ScheduleTemplateResponse] = Operation(
    id="getScheduleTemplate",
    method="GET",
    path="/sell/feed/v1/schedule_template/{schedule_template_id}",
    resource="schedules",
    name="get_template",
    params=(Param("schedule_template_id", "schedule_template_id", "path"),),
    response=ScheduleTemplateResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_schedule_templates: Operation[ScheduleTemplateCollection] = Operation(
    id="getScheduleTemplates",
    method="GET",
    path="/sell/feed/v1/schedule_template",
    resource="schedules",
    name="list_templates",
    params=(
        Param("feed_type", "feed_type", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=ScheduleTemplateCollection,
    returns_json=True,
    iterator="iter_templates",
    item=_models.ScheduleTemplateResponse,
    paging=NextLink(
        items="scheduleTemplates",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_schedules: Operation[UserScheduleCollection] = Operation(
    id="getSchedules",
    method="GET",
    path="/sell/feed/v1/schedule",
    resource="schedules",
    name="list",
    params=(
        Param("feed_type", "feed_type", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=UserScheduleCollection,
    returns_json=True,
    iterator="iter",
    item=_models.UserScheduleResponse,
    paging=NextLink(
        items="schedules",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_update_schedule: Operation[None] = Operation(
    id="updateSchedule",
    method="PUT",
    path="/sell/feed/v1/schedule/{schedule_id}",
    resource="schedules",
    name="update",
    params=(Param("schedule_id", "schedule_id", "path"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _create_schedule,
    _delete_schedule,
    _get_schedule,
    _get_schedule_template,
    _get_schedule_templates,
    _get_schedules,
    _update_schedule,
)


class SchedulesApi(Resource):
    @checked
    def create(
        self,
        body: Union[CreateUserScheduleRequest, Mapping[str, Any]],
    ) -> object:
        """Create a schedule that builds a report regularly."""
        return self._call(
            _create_schedule,
            _body=body,
        )

    @checked
    def delete(
        self,
        schedule_id: StrictStr,
    ) -> None:
        """Delete a schedule."""
        return self._call(
            _delete_schedule,
            schedule_id=schedule_id,
        )

    @checked
    def get(
        self,
        schedule_id: StrictStr,
    ) -> UserScheduleResponse:
        """Get one schedule."""
        return self._call(
            _get_schedule,
            schedule_id=schedule_id,
        )

    @checked
    def get_template(
        self,
        schedule_template_id: StrictStr,
    ) -> ScheduleTemplateResponse:
        """Get one schedule template."""
        return self._call(
            _get_schedule_template,
            schedule_template_id=schedule_template_id,
        )

    @checked
    def list_templates(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> ScheduleTemplateCollection:
        """List one page of schedule templates."""
        return self._call(
            _get_schedule_templates,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_templates(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.ScheduleTemplateResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_schedule_templates,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def list(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> UserScheduleCollection:
        """List one page of report schedules."""
        return self._call(
            _get_schedules,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.UserScheduleResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_schedules,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def update(
        self,
        schedule_id: StrictStr,
        body: Union[UpdateUserScheduleRequest, Mapping[str, Any]],
    ) -> None:
        """Update a schedule."""
        return self._call(
            _update_schedule,
            schedule_id=schedule_id,
            _body=body,
        )


class AsyncSchedulesApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CreateUserScheduleRequest, Mapping[str, Any]],
    ) -> object:
        """Create a schedule that builds a report regularly."""
        return await self._call(
            _create_schedule,
            _body=body,
        )

    @checked
    async def delete(
        self,
        schedule_id: StrictStr,
    ) -> None:
        """Delete a schedule."""
        return await self._call(
            _delete_schedule,
            schedule_id=schedule_id,
        )

    @checked
    async def get(
        self,
        schedule_id: StrictStr,
    ) -> UserScheduleResponse:
        """Get one schedule."""
        return await self._call(
            _get_schedule,
            schedule_id=schedule_id,
        )

    @checked
    async def get_template(
        self,
        schedule_template_id: StrictStr,
    ) -> ScheduleTemplateResponse:
        """Get one schedule template."""
        return await self._call(
            _get_schedule_template,
            schedule_template_id=schedule_template_id,
        )

    @checked
    async def list_templates(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> ScheduleTemplateCollection:
        """List one page of schedule templates."""
        return await self._call(
            _get_schedule_templates,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_templates(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ScheduleTemplateResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_schedule_templates,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    async def list(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> UserScheduleCollection:
        """List one page of report schedules."""
        return await self._call(
            _get_schedules,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        feed_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.UserScheduleResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_schedules,
            feed_type=feed_type,
            limit=limit,
            offset=offset,
        )

    @checked
    async def update(
        self,
        schedule_id: StrictStr,
        body: Union[UpdateUserScheduleRequest, Mapping[str, Any]],
    ) -> None:
        """Update a schedule."""
        return await self._call(
            _update_schedule,
            schedule_id=schedule_id,
            _body=body,
        )
