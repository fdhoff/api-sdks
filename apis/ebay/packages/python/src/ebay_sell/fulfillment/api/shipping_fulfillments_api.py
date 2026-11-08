# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.fulfillment.models.shipping_fulfillment import ShippingFulfillment
from ebay_sell.fulfillment.models.shipping_fulfillment_details import ShippingFulfillmentDetails
from ebay_sell.fulfillment.models.shipping_fulfillment_paged_collection import ShippingFulfillmentPagedCollection

_create_shipping_fulfillment: Operation[object] = Operation(
    id="createShippingFulfillment",
    method="POST",
    path="/sell/fulfillment/v1/order/{orderId}/shipping_fulfillment",
    resource="shipping_fulfillments",
    name="create",
    params=(Param("orderId", "order_id", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.fulfillment",)),),),
    host="api",
)
_get_shipping_fulfillment: Operation[ShippingFulfillment] = Operation(
    id="getShippingFulfillment",
    method="GET",
    path="/sell/fulfillment/v1/order/{orderId}/shipping_fulfillment/{fulfillmentId}",
    resource="shipping_fulfillments",
    name="get",
    params=(
        Param("fulfillmentId", "fulfillment_id", "path"),
        Param("orderId", "order_id", "path"),
    ),
    response=ShippingFulfillment,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_shipping_fulfillments: Operation[ShippingFulfillmentPagedCollection] = Operation(
    id="getShippingFulfillments",
    method="GET",
    path="/sell/fulfillment/v1/order/{orderId}/shipping_fulfillment",
    resource="shipping_fulfillments",
    name="list",
    params=(Param("orderId", "order_id", "path"),),
    response=ShippingFulfillmentPagedCollection,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _create_shipping_fulfillment,
    _get_shipping_fulfillment,
    _get_shipping_fulfillments,
)


class ShippingFulfillmentsApi(Resource):
    @checked
    def create(
        self,
        order_id: StrictStr,
        body: Union[ShippingFulfillmentDetails, Mapping[str, Any]],
    ) -> object:
        """Mark line items of an order shipped"""
        return self._call(
            _create_shipping_fulfillment,
            order_id=order_id,
            _body=body,
        )

    @checked
    def get(
        self,
        fulfillment_id: StrictStr,
        order_id: StrictStr,
    ) -> ShippingFulfillment:
        """Get one shipping fulfillment."""
        return self._call(
            _get_shipping_fulfillment,
            fulfillment_id=fulfillment_id,
            order_id=order_id,
        )

    @checked
    def list(
        self,
        order_id: StrictStr,
    ) -> ShippingFulfillmentPagedCollection:
        """List the shipping fulfillments of an order."""
        return self._call(
            _get_shipping_fulfillments,
            order_id=order_id,
        )


class AsyncShippingFulfillmentsApi(AsyncResource):
    @checked
    async def create(
        self,
        order_id: StrictStr,
        body: Union[ShippingFulfillmentDetails, Mapping[str, Any]],
    ) -> object:
        """Mark line items of an order shipped"""
        return await self._call(
            _create_shipping_fulfillment,
            order_id=order_id,
            _body=body,
        )

    @checked
    async def get(
        self,
        fulfillment_id: StrictStr,
        order_id: StrictStr,
    ) -> ShippingFulfillment:
        """Get one shipping fulfillment."""
        return await self._call(
            _get_shipping_fulfillment,
            fulfillment_id=fulfillment_id,
            order_id=order_id,
        )

    @checked
    async def list(
        self,
        order_id: StrictStr,
    ) -> ShippingFulfillmentPagedCollection:
        """List the shipping fulfillments of an order."""
        return await self._call(
            _get_shipping_fulfillments,
            order_id=order_id,
        )
