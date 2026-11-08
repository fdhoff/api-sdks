# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.notification import models as _models
from ebay_sell.notification.models.destination import Destination
from ebay_sell.notification.models.destination_request import DestinationRequest
from ebay_sell.notification.models.destination_search_response import DestinationSearchResponse

_create_destination: Operation[object] = Operation(
    id="createDestination",
    method="POST",
    path="/commerce/notification/v1/destination",
    resource="destinations",
    name="create",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_delete_destination: Operation[None] = Operation(
    id="deleteDestination",
    method="DELETE",
    path="/commerce/notification/v1/destination/{destination_id}",
    resource="destinations",
    name="delete",
    params=(Param("destination_id", "destination_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_destination: Operation[Destination] = Operation(
    id="getDestination",
    method="GET",
    path="/commerce/notification/v1/destination/{destination_id}",
    resource="destinations",
    name="get",
    params=(Param("destination_id", "destination_id", "path"),),
    response=Destination,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_destinations: Operation[DestinationSearchResponse] = Operation(
    id="getDestinations",
    method="GET",
    path="/commerce/notification/v1/destination",
    resource="destinations",
    name="list",
    params=(
        Param("continuation_token", "continuation_token", "query"),
        Param("limit", "limit", "query"),
    ),
    response=DestinationSearchResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Destination,
    paging=NextLink(
        items="destinations",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_update_destination: Operation[None] = Operation(
    id="updateDestination",
    method="PUT",
    path="/commerce/notification/v1/destination/{destination_id}",
    resource="destinations",
    name="update",
    params=(Param("destination_id", "destination_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (
    _create_destination,
    _delete_destination,
    _get_destination,
    _get_destinations,
    _update_destination,
)


class DestinationsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[DestinationRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Create a destination endpoint for notifications."""
        return self._call(
            _create_destination,
            _body=body,
        )

    @checked
    def delete(
        self,
        destination_id: StrictStr,
    ) -> None:
        """Delete a destination."""
        return self._call(
            _delete_destination,
            destination_id=destination_id,
        )

    @checked
    def get(
        self,
        destination_id: StrictStr,
    ) -> Destination:
        """Get one destination."""
        return self._call(
            _get_destination,
            destination_id=destination_id,
        )

    @checked
    def list(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> DestinationSearchResponse:
        """List one page of the app's notification destinations."""
        return self._call(
            _get_destinations,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> Iterator[_models.Destination]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_destinations,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def update(
        self,
        destination_id: StrictStr,
        body: Optional[Union[DestinationRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Update a destination."""
        return self._call(
            _update_destination,
            destination_id=destination_id,
            _body=body,
        )


class AsyncDestinationsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[DestinationRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Create a destination endpoint for notifications."""
        return await self._call(
            _create_destination,
            _body=body,
        )

    @checked
    async def delete(
        self,
        destination_id: StrictStr,
    ) -> None:
        """Delete a destination."""
        return await self._call(
            _delete_destination,
            destination_id=destination_id,
        )

    @checked
    async def get(
        self,
        destination_id: StrictStr,
    ) -> Destination:
        """Get one destination."""
        return await self._call(
            _get_destination,
            destination_id=destination_id,
        )

    @checked
    async def list(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> DestinationSearchResponse:
        """List one page of the app's notification destinations."""
        return await self._call(
            _get_destinations,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Destination]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_destinations,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    async def update(
        self,
        destination_id: StrictStr,
        body: Optional[Union[DestinationRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Update a destination."""
        return await self._call(
            _update_destination,
            destination_id=destination_id,
            _body=body,
        )
