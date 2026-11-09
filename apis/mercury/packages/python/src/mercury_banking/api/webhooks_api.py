# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.api_webhook_response import ApiWebhookResponse
from mercury_banking.models.api_webhooks_paginated_response import ApiWebhooksPaginatedResponse
from mercury_banking.models.create_webhook_params import CreateWebhookParams
from mercury_banking.models.update_webhook_params import UpdateWebhookParams
from mercury_banking.models.verify_webhook_params import VerifyWebhookParams

_create_webhook: Operation[ApiWebhookResponse] = Operation(
    id="createWebhook",
    method="POST",
    path="/webhooks",
    resource="webhooks",
    name="create",
    params=(),
    response=ApiWebhookResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_delete_webhook: Operation[None] = Operation(
    id="deleteWebhook",
    method="DELETE",
    path="/webhooks/{webhookEndpointId}",
    resource="webhooks",
    name="delete",
    params=(Param("webhookEndpointId", "webhook_endpoint_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_webhook: Operation[ApiWebhookResponse] = Operation(
    id="getWebhook",
    method="GET",
    path="/webhooks/{webhookEndpointId}",
    resource="webhooks",
    name="get",
    params=(Param("webhookEndpointId", "webhook_endpoint_id", "path"),),
    response=ApiWebhookResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_webhooks: Operation[ApiWebhooksPaginatedResponse] = Operation(
    id="getWebhooks",
    method="GET",
    path="/webhooks",
    resource="webhooks",
    name="list",
    params=(
        Param("status", "status", "query"),
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=ApiWebhooksPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.ApiWebhookResponse,
    paging=Cursor(items="webhooks", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_update_webhook: Operation[ApiWebhookResponse] = Operation(
    id="updateWebhook",
    method="POST",
    path="/webhooks/{webhookEndpointId}",
    resource="webhooks",
    name="update",
    params=(Param("webhookEndpointId", "webhook_endpoint_id", "path"),),
    response=ApiWebhookResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_verify_webhook: Operation[None] = Operation(
    id="verifyWebhook",
    method="POST",
    path="/webhooks/{webhookEndpointId}/verify",
    resource="webhooks",
    name="send_test_event",
    params=(Param("webhookEndpointId", "webhook_endpoint_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _create_webhook,
    _delete_webhook,
    _get_webhook,
    _get_webhooks,
    _update_webhook,
    _verify_webhook,
)


class WebhooksApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[CreateWebhookParams, Mapping[str, Any]]] = None,
    ) -> ApiWebhookResponse:
        """Register a webhook endpoint."""
        return self._call(
            _create_webhook,
            _body=body,
        )

    @checked
    def delete(
        self,
        webhook_endpoint_id: UUID,
    ) -> None:
        """Delete a webhook endpoint."""
        return self._call(
            _delete_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
        )

    @checked
    def get(
        self,
        webhook_endpoint_id: UUID,
    ) -> ApiWebhookResponse:
        """Get one webhook endpoint."""
        return self._call(
            _get_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
        )

    @checked
    def list(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiWebhooksPaginatedResponse:
        """List one page of webhook endpoints."""
        return self._call(
            _get_webhooks,
            status=status,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ApiWebhookResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_webhooks,
            status=status,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def update(
        self,
        webhook_endpoint_id: UUID,
        body: Optional[Union[UpdateWebhookParams, Mapping[str, Any]]] = None,
    ) -> ApiWebhookResponse:
        """Update a webhook endpoint."""
        return self._call(
            _update_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
            _body=body,
        )

    @checked
    def send_test_event(
        self,
        webhook_endpoint_id: UUID,
        body: Optional[Union[VerifyWebhookParams, Mapping[str, Any]]] = None,
    ) -> None:
        """Send a test event to a webhook endpoint."""
        return self._call(
            _verify_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
            _body=body,
        )


class AsyncWebhooksApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[CreateWebhookParams, Mapping[str, Any]]] = None,
    ) -> ApiWebhookResponse:
        """Register a webhook endpoint."""
        return await self._call(
            _create_webhook,
            _body=body,
        )

    @checked
    async def delete(
        self,
        webhook_endpoint_id: UUID,
    ) -> None:
        """Delete a webhook endpoint."""
        return await self._call(
            _delete_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
        )

    @checked
    async def get(
        self,
        webhook_endpoint_id: UUID,
    ) -> ApiWebhookResponse:
        """Get one webhook endpoint."""
        return await self._call(
            _get_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
        )

    @checked
    async def list(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiWebhooksPaginatedResponse:
        """List one page of webhook endpoints."""
        return await self._call(
            _get_webhooks,
            status=status,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ApiWebhookResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_webhooks,
            status=status,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def update(
        self,
        webhook_endpoint_id: UUID,
        body: Optional[Union[UpdateWebhookParams, Mapping[str, Any]]] = None,
    ) -> ApiWebhookResponse:
        """Update a webhook endpoint."""
        return await self._call(
            _update_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
            _body=body,
        )

    @checked
    async def send_test_event(
        self,
        webhook_endpoint_id: UUID,
        body: Optional[Union[VerifyWebhookParams, Mapping[str, Any]]] = None,
    ) -> None:
        """Send a test event to a webhook endpoint."""
        return await self._call(
            _verify_webhook,
            webhook_endpoint_id=webhook_endpoint_id,
            _body=body,
        )
