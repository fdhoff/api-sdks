# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import Field, StrictBool, StrictStr
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.create_receipt_shipment_request import CreateReceiptShipmentRequest
from etsy_seller.models.shop_receipt import ShopReceipt
from etsy_seller.models.shop_receipts import ShopReceipts

_create_receipt_shipment: Operation[ShopReceipt] = Operation(
    id="createReceiptShipment",
    method="POST",
    path="/v3/application/shops/{shop_id}/receipts/{receipt_id}/tracking",
    resource="receipts",
    name="create_shipment",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("receipt_id", "receipt_id", "path"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopReceipt,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_w",)),
        ),
    ),
)
_get_shop_receipt: Operation[ShopReceipt] = Operation(
    id="getShopReceipt",
    method="GET",
    path="/v3/application/shops/{shop_id}/receipts/{receipt_id}",
    resource="receipts",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("receipt_id", "receipt_id", "path"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopReceipt,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_shop_receipts: Operation[ShopReceipts] = Operation(
    id="getShopReceipts",
    method="GET",
    path="/v3/application/shops/{shop_id}/receipts",
    resource="receipts",
    name="list",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("min_created", "min_created", "query"),
        Param("max_created", "max_created", "query"),
        Param("min_last_modified", "min_last_modified", "query"),
        Param("max_last_modified", "max_last_modified", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort_on", "sort_on", "query"),
        Param("sort_order", "sort_order", "query"),
        Param("was_paid", "was_paid", "query"),
        Param("was_shipped", "was_shipped", "query"),
        Param("was_delivered", "was_delivered", "query"),
        Param("was_canceled", "was_canceled", "query"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopReceipts,
    returns_json=True,
    iterator="iter",
    item=_models.ShopReceipt,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_update_shop_receipt: Operation[ShopReceipt] = Operation(
    id="updateShopReceipt",
    method="PUT",
    path="/v3/application/shops/{shop_id}/receipts/{receipt_id}",
    resource="receipts",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("receipt_id", "receipt_id", "path"),
        Param("legacy", "legacy", "query"),
        Param("was_shipped", "was_shipped", "urlencoded"),
        Param("was_paid", "was_paid", "urlencoded"),
    ),
    response=ShopReceipt,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_w",)),
        ),
    ),
)

OPERATIONS = (
    _create_receipt_shipment,
    _get_shop_receipt,
    _get_shop_receipts,
    _update_shop_receipt,
)


class ReceiptsApi(Resource):
    @checked
    def create_shipment(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[CreateReceiptShipmentRequest, Mapping[str, Any]]] = None,
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceipt:
        """Add tracking to a receipt and mark it shipped."""
        return self._call(
            _create_receipt_shipment,
            shop_id=shop_id,
            receipt_id=receipt_id,
            _body=body,
            legacy=legacy,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceipt:
        """Get one receipt."""
        return self._call(
            _get_shop_receipt,
            shop_id=shop_id,
            receipt_id=receipt_id,
            legacy=legacy,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        min_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        was_paid: Optional[StrictBool] = None,
        was_shipped: Optional[StrictBool] = None,
        was_delivered: Optional[StrictBool] = None,
        was_canceled: Optional[StrictBool] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceipts:
        """List one page of a shop&#39;s receipts."""
        return self._call(
            _get_shop_receipts,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            min_last_modified=min_last_modified,
            max_last_modified=max_last_modified,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            was_paid=was_paid,
            was_shipped=was_shipped,
            was_delivered=was_delivered,
            was_canceled=was_canceled,
            legacy=legacy,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        min_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        was_paid: Optional[StrictBool] = None,
        was_shipped: Optional[StrictBool] = None,
        was_delivered: Optional[StrictBool] = None,
        was_canceled: Optional[StrictBool] = None,
        legacy: Optional[StrictBool] = None,
    ) -> Iterator[_models.ShopReceipt]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_receipts,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            min_last_modified=min_last_modified,
            max_last_modified=max_last_modified,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            was_paid=was_paid,
            was_shipped=was_shipped,
            was_delivered=was_delivered,
            was_canceled=was_canceled,
            legacy=legacy,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
        was_shipped: Optional[StrictBool] = None,
        was_paid: Optional[StrictBool] = None,
    ) -> ShopReceipt:
        """Update a receipt&#39;s shipped or paid state."""
        return self._call(
            _update_shop_receipt,
            shop_id=shop_id,
            receipt_id=receipt_id,
            legacy=legacy,
            was_shipped=was_shipped,
            was_paid=was_paid,
        )


class AsyncReceiptsApi(AsyncResource):
    @checked
    async def create_shipment(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[CreateReceiptShipmentRequest, Mapping[str, Any]]] = None,
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceipt:
        """Add tracking to a receipt and mark it shipped."""
        return await self._call(
            _create_receipt_shipment,
            shop_id=shop_id,
            receipt_id=receipt_id,
            _body=body,
            legacy=legacy,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceipt:
        """Get one receipt."""
        return await self._call(
            _get_shop_receipt,
            shop_id=shop_id,
            receipt_id=receipt_id,
            legacy=legacy,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        min_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        was_paid: Optional[StrictBool] = None,
        was_shipped: Optional[StrictBool] = None,
        was_delivered: Optional[StrictBool] = None,
        was_canceled: Optional[StrictBool] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceipts:
        """List one page of a shop&#39;s receipts."""
        return await self._call(
            _get_shop_receipts,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            min_last_modified=min_last_modified,
            max_last_modified=max_last_modified,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            was_paid=was_paid,
            was_shipped=was_shipped,
            was_delivered=was_delivered,
            was_canceled=was_canceled,
            legacy=legacy,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        min_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_last_modified: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort_on: Optional[StrictStr] = None,
        sort_order: Optional[StrictStr] = None,
        was_paid: Optional[StrictBool] = None,
        was_shipped: Optional[StrictBool] = None,
        was_delivered: Optional[StrictBool] = None,
        was_canceled: Optional[StrictBool] = None,
        legacy: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.ShopReceipt]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_receipts,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            min_last_modified=min_last_modified,
            max_last_modified=max_last_modified,
            limit=limit,
            offset=offset,
            sort_on=sort_on,
            sort_order=sort_order,
            was_paid=was_paid,
            was_shipped=was_shipped,
            was_delivered=was_delivered,
            was_canceled=was_canceled,
            legacy=legacy,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
        was_shipped: Optional[StrictBool] = None,
        was_paid: Optional[StrictBool] = None,
    ) -> ShopReceipt:
        """Update a receipt&#39;s shipped or paid state."""
        return await self._call(
            _update_shop_receipt,
            shop_id=shop_id,
            receipt_id=receipt_id,
            legacy=legacy,
            was_shipped=was_shipped,
            was_paid=was_paid,
        )
