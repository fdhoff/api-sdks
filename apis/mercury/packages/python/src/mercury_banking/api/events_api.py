# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.api_event_response import ApiEventResponse
from mercury_banking.models.api_events_paginated_response import ApiEventsPaginatedResponse

_get_event: Operation[ApiEventResponse] = Operation(
    id="getEvent",
    method="GET",
    path="/events/{eventId}",
    resource="events",
    name="get",
    params=(Param("eventId", "event_id", "path"),),
    response=ApiEventResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_events: Operation[ApiEventsPaginatedResponse] = Operation(
    id="getEvents",
    method="GET",
    path="/events",
    resource="events",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
        Param("resourceType", "resource_type", "query"),
        Param("resourceId", "resource_id", "query"),
    ),
    response=ApiEventsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.ApiEventResponse,
    paging=Cursor(items="events", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_event,
    _get_events,
)


class EventsApi(Resource):
    @checked
    def get(
        self,
        event_id: UUID,
    ) -> ApiEventResponse:
        """Get one event."""
        return self._call(
            _get_event,
            event_id=event_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
        resource_type: Optional[StrictStr] = None,
        resource_id: Optional[UUID] = None,
    ) -> ApiEventsPaginatedResponse:
        """List one page of events."""
        return self._call(
            _get_events,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            resource_type=resource_type,
            resource_id=resource_id,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
        resource_type: Optional[StrictStr] = None,
        resource_id: Optional[UUID] = None,
    ) -> Iterator[_models.ApiEventResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_events,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            resource_type=resource_type,
            resource_id=resource_id,
        )


class AsyncEventsApi(AsyncResource):
    @checked
    async def get(
        self,
        event_id: UUID,
    ) -> ApiEventResponse:
        """Get one event."""
        return await self._call(
            _get_event,
            event_id=event_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
        resource_type: Optional[StrictStr] = None,
        resource_id: Optional[UUID] = None,
    ) -> ApiEventsPaginatedResponse:
        """List one page of events."""
        return await self._call(
            _get_events,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            resource_type=resource_type,
            resource_id=resource_id,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
        resource_type: Optional[StrictStr] = None,
        resource_id: Optional[UUID] = None,
    ) -> AsyncIterator[_models.ApiEventResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_events,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            resource_type=resource_type,
            resource_id=resource_id,
        )
