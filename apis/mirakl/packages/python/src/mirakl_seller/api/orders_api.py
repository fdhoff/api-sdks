# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated

from mirakl_seller import models as _models
from mirakl_seller._runtime import (
    AsyncDownload,
    AsyncResource,
    Download,
    FileInput,
    Job,
    Offset,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mirakl_seller.models.or04_request import OR04Request
from mirakl_seller.models.or04_response200 import OR04Response200
from mirakl_seller.models.or07_request import OR07Request
from mirakl_seller.models.or07_response200 import OR07Response200
from mirakl_seller.models.or11_response200 import OR11Response200
from mirakl_seller.models.or13_request import OR13Request
from mirakl_seller.models.or13_response200 import OR13Response200
from mirakl_seller.models.or14_response200 import OR14Response200
from mirakl_seller.models.or21_request import OR21Request
from mirakl_seller.models.or23_request import OR23Request
from mirakl_seller.models.or28_request import OR28Request
from mirakl_seller.models.or28_response200 import OR28Response200
from mirakl_seller.models.or30_request import OR30Request
from mirakl_seller.models.or30_response200 import OR30Response200
from mirakl_seller.models.or31_request import OR31Request
from mirakl_seller.models.or31_response200 import OR31Response200
from mirakl_seller.models.or32_request import OR32Request
from mirakl_seller.models.or32_response200 import OR32Response200
from mirakl_seller.models.or33_request import OR33Request
from mirakl_seller.models.or43_request_multipart_form_data_thread_input import OR43RequestMultipartFormDataThreadInput
from mirakl_seller.models.or43_response201 import OR43Response201
from mirakl_seller.models.or51_response200 import OR51Response200
from mirakl_seller.models.or64_request import OR64Request
from mirakl_seller.models.or72_response200 import OR72Response200
from mirakl_seller.models.or74_request_multipart_form_data_order_documents import (
    OR74RequestMultipartFormDataOrderDocuments,
)
from mirakl_seller.models.or74_response200 import OR74Response200
from mirakl_seller.models.or75_response200 import OR75Response200

_o_r04: Operation[OR04Response200] = Operation(
    id="OR04",
    method="PUT",
    path="/api/orders",
    resource="orders",
    name="update",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OR04Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_EDIT",
                ),
            ),
        ),
    ),
)
_o_r07: Operation[OR07Response200] = Operation(
    id="OR07",
    method="PUT",
    path="/api/orders/shipping_from",
    resource="orders",
    name="update_shipping_origin",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OR07Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIP",
                ),
            ),
        ),
    ),
)
_o_r11: Operation[OR11Response200] = Operation(
    id="OR11",
    method="GET",
    path="/api/orders",
    resource="orders",
    name="list",
    params=(
        Param("order_ids", "order_ids", "query"),
        Param("order_references_for_customer", "order_references_for_customer", "query"),
        Param("order_references_for_seller", "order_references_for_seller", "query"),
        Param("order_state_codes", "order_state_codes", "query"),
        Param("channel_codes", "channel_codes", "query"),
        Param("only_null_channel", "only_null_channel", "query"),
        Param("start_date", "start_date", "query"),
        Param("end_date", "end_date", "query"),
        Param("start_update_date", "start_update_date", "query"),
        Param("end_update_date", "end_update_date", "query"),
        Param("customer_debited", "customer_debited", "query"),
        Param("payment_workflow", "payment_workflow", "query"),
        Param("has_incident", "has_incident", "query"),
        Param("fulfillment_center_code", "fulfillment_center_code", "query"),
        Param("order_tax_mode", "order_tax_mode", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("max", "max", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("order", "order", "query"),
    ),
    response=OR11Response200,
    returns_json=True,
    iterator="iter",
    item=_models.OR11Response200Orders,
    paging=Offset(items="orders", total="total_count", offset="offset"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_READ",
                ),
            ),
        ),
    ),
)
_o_r13: Operation[OR13Response200] = Operation(
    id="OR13",
    method="POST",
    path="/api/orders/async-export",
    resource="orders",
    name="export",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OR13Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_READ",
                ),
            ),
        ),
    ),
)
_o_r14: Operation[OR14Response200] = Operation(
    id="OR14",
    method="GET",
    path="/api/orders/async-export/status/{tracking_id}",
    resource="orders",
    name="get_export",
    params=(
        Param("tracking_id", "tracking_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=OR14Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_READ",
                ),
            ),
        ),
    ),
    job=Job(state="status", done=("COMPLETED",), failed=("FAILED",)),
)
_o_r21: Operation[None] = Operation(
    id="OR21",
    method="PUT",
    path="/api/orders/{order_id}/accept",
    resource="orders",
    name="accept",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_ACCEPT",
                ),
            ),
        ),
    ),
)
_o_r23: Operation[None] = Operation(
    id="OR23",
    method="PUT",
    path="/api/orders/{order_id}/tracking",
    resource="orders",
    name="update_tracking",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_TRACKING_WRITE",
                ),
            ),
        ),
    ),
)
_o_r24: Operation[None] = Operation(
    id="OR24",
    method="PUT",
    path="/api/orders/{order_id}/ship",
    resource="orders",
    name="ship",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIP",
                ),
            ),
        ),
    ),
)
_o_r28: Operation[OR28Response200] = Operation(
    id="OR28",
    method="PUT",
    path="/api/orders/refund",
    resource="orders",
    name="refund",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OR28Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_REFUND_REQUEST",
                    "ROLE_PARTNER_ORDER_REFUND",
                ),
            ),
        ),
    ),
)
_o_r29: Operation[None] = Operation(
    id="OR29",
    method="PUT",
    path="/api/orders/{order_id}/cancel",
    resource="orders",
    name="cancel",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_CANCEL",
                ),
            ),
        ),
    ),
)
_o_r30: Operation[OR30Response200] = Operation(
    id="OR30",
    method="PUT",
    path="/api/orders/cancel",
    resource="orders",
    name="cancel_lines",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OR30Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_CANCEL",
                ),
            ),
        ),
    ),
)
_o_r31: Operation[OR31Response200] = Operation(
    id="OR31",
    method="PUT",
    path="/api/orders/{order_id}/additional_fields",
    resource="orders",
    name="update_custom_fields",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=OR31Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_ADDITIONAL_FIELD_UPDATE",
                ),
            ),
        ),
    ),
)
_o_r32: Operation[OR32Response200] = Operation(
    id="OR32",
    method="PUT",
    path="/api/orders/adjust",
    resource="orders",
    name="adjust_lines",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OR32Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_ADJUST",
                ),
            ),
        ),
    ),
)
_o_r33: Operation[None] = Operation(
    id="OR33",
    method="PUT",
    path="/api/orders/{order_id}/cancel-order-lines",
    resource="orders",
    name="fully_cancel_lines",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_CANCEL",
                ),
            ),
        ),
    ),
)
_o_r43: Operation[OR43Response201] = Operation(
    id="OR43",
    method="POST",
    path="/api/orders/{order_id}/threads",
    resource="orders",
    name="create_thread",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("files", "files", "form"),
        Param("thread_input", "thread_input", "form"),
    ),
    response=OR43Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_MESSAGE_WRITE",
                ),
            ),
        ),
    ),
)
_o_r51: Operation[OR51Response200] = Operation(
    id="OR51",
    method="GET",
    path="/api/orders/{order_id}/evaluation",
    resource="orders",
    name="get_evaluation",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=OR51Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_EVALUATION_READ",
                ),
            ),
        ),
    ),
)
_o_r64: Operation[None] = Operation(
    id="OR64",
    method="PUT",
    path="/api/orders/{order_id}/lines/{line}/resolve_incident",
    resource="orders",
    name="resolve_incident",
    params=(
        Param("order_id", "order_id", "path"),
        Param("line", "line", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_INCIDENT_RESOLVE",
                ),
            ),
        ),
    ),
)
_o_r72: Operation[OR72Response200] = Operation(
    id="OR72",
    method="GET",
    path="/api/orders/documents",
    resource="orders",
    name="list_documents",
    params=(
        Param("order_ids", "order_ids", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=OR72Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_o_r73: Operation[None] = Operation(
    id="OR73",
    method="GET",
    path="/api/orders/documents/download",
    resource="orders",
    name="download_documents",
    params=(
        Param("order_ids", "order_ids", "query"),
        Param("document_ids", "document_ids", "query"),
        Param("document_codes", "document_codes", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_o_r74: Operation[OR74Response200] = Operation(
    id="OR74",
    method="POST",
    path="/api/orders/{order_id}/documents",
    resource="orders",
    name="upload_documents",
    params=(
        Param("order_id", "order_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("files", "files", "form"),
        Param("order_documents", "order_documents", "form"),
    ),
    response=OR74Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_DOCUMENT_WRITE",
                ),
            ),
        ),
    ),
)
_o_r75: Operation[OR75Response200] = Operation(
    id="OR75",
    method="GET",
    path="/api/orders/taxes",
    resource="orders",
    name="list_taxes",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=OR75Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SETTINGS_READ",
                ),
            ),
        ),
    ),
)
_o_r76: Operation[None] = Operation(
    id="OR76",
    method="DELETE",
    path="/api/orders/documents/{document_id}",
    resource="orders",
    name="delete_document",
    params=(
        Param("document_id", "document_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_DOCUMENT_DELETE",
                ),
            ),
        ),
    ),
)

OPERATIONS = (
    _o_r04,
    _o_r07,
    _o_r11,
    _o_r13,
    _o_r14,
    _o_r21,
    _o_r23,
    _o_r24,
    _o_r28,
    _o_r29,
    _o_r30,
    _o_r31,
    _o_r32,
    _o_r33,
    _o_r43,
    _o_r51,
    _o_r64,
    _o_r72,
    _o_r73,
    _o_r74,
    _o_r75,
    _o_r76,
)


class OrdersApi(Resource):
    @checked
    def update(
        self,
        body: Optional[Union[OR04Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR04Response200:
        """Update fields on several orders (OR04)."""
        return self._call(
            _o_r04,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def update_shipping_origin(
        self,
        body: Optional[Union[OR07Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR07Response200:
        """Update the shipping origin of order lines (OR07)."""
        return self._call(
            _o_r07,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list(
        self,
        *,
        order_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_customer: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_seller: Optional[Annotated[str, Field(strict=True)]] = None,
        order_state_codes: Optional[StrictStr] = None,
        channel_codes: Optional[Annotated[str, Field(strict=True)]] = None,
        only_null_channel: Optional[StrictBool] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        start_update_date: Optional[datetime] = None,
        end_update_date: Optional[datetime] = None,
        customer_debited: Optional[StrictBool] = None,
        payment_workflow: Optional[StrictStr] = None,
        has_incident: Optional[StrictBool] = None,
        fulfillment_center_code: Optional[List[Annotated[str, Field(strict=True)]]] = None,
        order_tax_mode: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> OR11Response200:
        """List one page of orders (OR11)."""
        return self._call(
            _o_r11,
            order_ids=order_ids,
            order_references_for_customer=order_references_for_customer,
            order_references_for_seller=order_references_for_seller,
            order_state_codes=order_state_codes,
            channel_codes=channel_codes,
            only_null_channel=only_null_channel,
            start_date=start_date,
            end_date=end_date,
            start_update_date=start_update_date,
            end_update_date=end_update_date,
            customer_debited=customer_debited,
            payment_workflow=payment_workflow,
            has_incident=has_incident,
            fulfillment_center_code=fulfillment_center_code,
            order_tax_mode=order_tax_mode,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        order_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_customer: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_seller: Optional[Annotated[str, Field(strict=True)]] = None,
        order_state_codes: Optional[StrictStr] = None,
        channel_codes: Optional[Annotated[str, Field(strict=True)]] = None,
        only_null_channel: Optional[StrictBool] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        start_update_date: Optional[datetime] = None,
        end_update_date: Optional[datetime] = None,
        customer_debited: Optional[StrictBool] = None,
        payment_workflow: Optional[StrictStr] = None,
        has_incident: Optional[StrictBool] = None,
        fulfillment_center_code: Optional[List[Annotated[str, Field(strict=True)]]] = None,
        order_tax_mode: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.OR11Response200Orders]:
        """Iterate every item across all pages."""
        return self._paginate(
            _o_r11,
            order_ids=order_ids,
            order_references_for_customer=order_references_for_customer,
            order_references_for_seller=order_references_for_seller,
            order_state_codes=order_state_codes,
            channel_codes=channel_codes,
            only_null_channel=only_null_channel,
            start_date=start_date,
            end_date=end_date,
            start_update_date=start_update_date,
            end_update_date=end_update_date,
            customer_debited=customer_debited,
            payment_workflow=payment_workflow,
            has_incident=has_incident,
            fulfillment_center_code=fulfillment_center_code,
            order_tax_mode=order_tax_mode,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def export(
        self,
        body: Optional[Union[OR13Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR13Response200:
        """Start an export of orders as JSON files (OR13)."""
        return self._call(
            _o_r13,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def get_export(
        self,
        tracking_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR14Response200:
        """Get the status of an order export (OR14)."""
        return self._call(
            _o_r14,
            tracking_id=tracking_id,
            shop_id=shop_id,
        )

    @checked
    def wait_for_export(
        self,
        tracking_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> OR14Response200:
        """Poll every `interval` seconds until the job that `export` started ends, and return its last status,
        done or failed. Pass the `tracking_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass."""
        return self._wait(
            _o_r14,
            interval=interval,
            timeout=timeout,
            tracking_id=tracking_id,
        )

    @checked
    def accept(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR21Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Accept or refuse an order's lines (OR21)."""
        return self._call(
            _o_r21,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def update_tracking(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR23Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Update an order's carrier tracking (OR23)."""
        return self._call(
            _o_r23,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def ship(
        self,
        order_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Confirm that an order has shipped (OR24)."""
        return self._call(
            _o_r24,
            order_id=order_id,
            shop_id=shop_id,
        )

    @checked
    def refund(
        self,
        body: Optional[Union[OR28Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR28Response200:
        """Refund order lines (OR28)."""
        return self._call(
            _o_r28,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def cancel(
        self,
        order_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Cancel a whole order (OR29)."""
        return self._call(
            _o_r29,
            order_id=order_id,
            shop_id=shop_id,
        )

    @checked
    def cancel_lines(
        self,
        body: Optional[Union[OR30Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR30Response200:
        """Cancel quantities or amounts on order lines (OR30)."""
        return self._call(
            _o_r30,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def update_custom_fields(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR31Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR31Response200:
        """Update the custom fields of an order and its lines (OR31)."""
        return self._call(
            _o_r31,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def adjust_lines(
        self,
        body: Optional[Union[OR32Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR32Response200:
        """Adjust order lines (OR32)."""
        return self._call(
            _o_r32,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def fully_cancel_lines(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR33Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Fully cancel some of an order's lines (OR33)."""
        return self._call(
            _o_r33,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def create_thread(
        self,
        order_id: StrictStr,
        *,
        thread_input: OR43RequestMultipartFormDataThreadInput,
        shop_id: Optional[StrictInt] = None,
        files: Optional[List[FileInput]] = None,
    ) -> OR43Response201:
        """Start a message thread on an order (OR43)."""
        return self._call(
            _o_r43,
            order_id=order_id,
            shop_id=shop_id,
            files=files,
            thread_input=thread_input,
        )

    @checked
    def get_evaluation(
        self,
        order_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR51Response200:
        """Get an order's evaluation (OR51)."""
        return self._call(
            _o_r51,
            order_id=order_id,
            shop_id=shop_id,
        )

    @checked
    def resolve_incident(
        self,
        order_id: StrictStr,
        line: StrictStr,
        body: Optional[Union[OR64Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Mark an order line's incident as resolved (OR64)."""
        return self._call(
            _o_r64,
            order_id=order_id,
            line=line,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list_documents(
        self,
        *,
        order_ids: Annotated[str, Field(strict=True)],
        shop_id: Optional[StrictInt] = None,
    ) -> OR72Response200:
        """List the documents on orders (OR72)."""
        return self._call(
            _o_r72,
            order_ids=order_ids,
            shop_id=shop_id,
        )

    @checked
    def download_documents(
        self,
        *,
        order_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        document_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        document_codes: Optional[Annotated[str, Field(strict=True)]] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download one or more order documents (OR73). Close the download, or read it in a `with` block."""
        return self._download(
            _o_r73,
            order_ids=order_ids,
            document_ids=document_ids,
            document_codes=document_codes,
            shop_id=shop_id,
        )

    @checked
    def upload_documents(
        self,
        order_id: StrictStr,
        *,
        files: List[FileInput],
        order_documents: OR74RequestMultipartFormDataOrderDocuments,
        shop_id: Optional[StrictInt] = None,
    ) -> OR74Response200:
        """Upload documents to an order (OR74)."""
        return self._call(
            _o_r74,
            order_id=order_id,
            shop_id=shop_id,
            files=files,
            order_documents=order_documents,
        )

    @checked
    def list_taxes(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR75Response200:
        """List the order taxes the platform uses (OR75)."""
        return self._call(
            _o_r75,
            shop_id=shop_id,
        )

    @checked
    def delete_document(
        self,
        document_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Delete an order document (OR76)."""
        return self._call(
            _o_r76,
            document_id=document_id,
            shop_id=shop_id,
        )


class AsyncOrdersApi(AsyncResource):
    @checked
    async def update(
        self,
        body: Optional[Union[OR04Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR04Response200:
        """Update fields on several orders (OR04)."""
        return await self._call(
            _o_r04,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def update_shipping_origin(
        self,
        body: Optional[Union[OR07Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR07Response200:
        """Update the shipping origin of order lines (OR07)."""
        return await self._call(
            _o_r07,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list(
        self,
        *,
        order_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_customer: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_seller: Optional[Annotated[str, Field(strict=True)]] = None,
        order_state_codes: Optional[StrictStr] = None,
        channel_codes: Optional[Annotated[str, Field(strict=True)]] = None,
        only_null_channel: Optional[StrictBool] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        start_update_date: Optional[datetime] = None,
        end_update_date: Optional[datetime] = None,
        customer_debited: Optional[StrictBool] = None,
        payment_workflow: Optional[StrictStr] = None,
        has_incident: Optional[StrictBool] = None,
        fulfillment_center_code: Optional[List[Annotated[str, Field(strict=True)]]] = None,
        order_tax_mode: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> OR11Response200:
        """List one page of orders (OR11)."""
        return await self._call(
            _o_r11,
            order_ids=order_ids,
            order_references_for_customer=order_references_for_customer,
            order_references_for_seller=order_references_for_seller,
            order_state_codes=order_state_codes,
            channel_codes=channel_codes,
            only_null_channel=only_null_channel,
            start_date=start_date,
            end_date=end_date,
            start_update_date=start_update_date,
            end_update_date=end_update_date,
            customer_debited=customer_debited,
            payment_workflow=payment_workflow,
            has_incident=has_incident,
            fulfillment_center_code=fulfillment_center_code,
            order_tax_mode=order_tax_mode,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        order_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_customer: Optional[Annotated[str, Field(strict=True)]] = None,
        order_references_for_seller: Optional[Annotated[str, Field(strict=True)]] = None,
        order_state_codes: Optional[StrictStr] = None,
        channel_codes: Optional[Annotated[str, Field(strict=True)]] = None,
        only_null_channel: Optional[StrictBool] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        start_update_date: Optional[datetime] = None,
        end_update_date: Optional[datetime] = None,
        customer_debited: Optional[StrictBool] = None,
        payment_workflow: Optional[StrictStr] = None,
        has_incident: Optional[StrictBool] = None,
        fulfillment_center_code: Optional[List[Annotated[str, Field(strict=True)]]] = None,
        order_tax_mode: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
        max: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        sort: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.OR11Response200Orders]:
        """Iterate every item across all pages."""
        return self._paginate(
            _o_r11,
            order_ids=order_ids,
            order_references_for_customer=order_references_for_customer,
            order_references_for_seller=order_references_for_seller,
            order_state_codes=order_state_codes,
            channel_codes=channel_codes,
            only_null_channel=only_null_channel,
            start_date=start_date,
            end_date=end_date,
            start_update_date=start_update_date,
            end_update_date=end_update_date,
            customer_debited=customer_debited,
            payment_workflow=payment_workflow,
            has_incident=has_incident,
            fulfillment_center_code=fulfillment_center_code,
            order_tax_mode=order_tax_mode,
            shop_id=shop_id,
            max=max,
            offset=offset,
            sort=sort,
            order=order,
        )

    @checked
    async def export(
        self,
        body: Optional[Union[OR13Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR13Response200:
        """Start an export of orders as JSON files (OR13)."""
        return await self._call(
            _o_r13,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def get_export(
        self,
        tracking_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR14Response200:
        """Get the status of an order export (OR14)."""
        return await self._call(
            _o_r14,
            tracking_id=tracking_id,
            shop_id=shop_id,
        )

    @checked
    async def wait_for_export(
        self,
        tracking_id: StrictStr,
        *,
        interval: float = 60.0,
        timeout: float = 3600.0,
    ) -> OR14Response200:
        """Poll every `interval` seconds until the job that `export` started ends, and return its last status,
        done or failed. Pass the `tracking_id` it returned. Raises `JobTimeoutError` once `timeout` seconds pass, and
        stops when the task is cancelled."""
        return await self._wait(
            _o_r14,
            interval=interval,
            timeout=timeout,
            tracking_id=tracking_id,
        )

    @checked
    async def accept(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR21Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Accept or refuse an order's lines (OR21)."""
        return await self._call(
            _o_r21,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def update_tracking(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR23Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Update an order's carrier tracking (OR23)."""
        return await self._call(
            _o_r23,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def ship(
        self,
        order_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Confirm that an order has shipped (OR24)."""
        return await self._call(
            _o_r24,
            order_id=order_id,
            shop_id=shop_id,
        )

    @checked
    async def refund(
        self,
        body: Optional[Union[OR28Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR28Response200:
        """Refund order lines (OR28)."""
        return await self._call(
            _o_r28,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def cancel(
        self,
        order_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Cancel a whole order (OR29)."""
        return await self._call(
            _o_r29,
            order_id=order_id,
            shop_id=shop_id,
        )

    @checked
    async def cancel_lines(
        self,
        body: Optional[Union[OR30Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR30Response200:
        """Cancel quantities or amounts on order lines (OR30)."""
        return await self._call(
            _o_r30,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def update_custom_fields(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR31Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR31Response200:
        """Update the custom fields of an order and its lines (OR31)."""
        return await self._call(
            _o_r31,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def adjust_lines(
        self,
        body: Optional[Union[OR32Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR32Response200:
        """Adjust order lines (OR32)."""
        return await self._call(
            _o_r32,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def fully_cancel_lines(
        self,
        order_id: StrictStr,
        body: Optional[Union[OR33Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Fully cancel some of an order's lines (OR33)."""
        return await self._call(
            _o_r33,
            order_id=order_id,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def create_thread(
        self,
        order_id: StrictStr,
        *,
        thread_input: OR43RequestMultipartFormDataThreadInput,
        shop_id: Optional[StrictInt] = None,
        files: Optional[List[FileInput]] = None,
    ) -> OR43Response201:
        """Start a message thread on an order (OR43)."""
        return await self._call(
            _o_r43,
            order_id=order_id,
            shop_id=shop_id,
            files=files,
            thread_input=thread_input,
        )

    @checked
    async def get_evaluation(
        self,
        order_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR51Response200:
        """Get an order's evaluation (OR51)."""
        return await self._call(
            _o_r51,
            order_id=order_id,
            shop_id=shop_id,
        )

    @checked
    async def resolve_incident(
        self,
        order_id: StrictStr,
        line: StrictStr,
        body: Optional[Union[OR64Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Mark an order line's incident as resolved (OR64)."""
        return await self._call(
            _o_r64,
            order_id=order_id,
            line=line,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list_documents(
        self,
        *,
        order_ids: Annotated[str, Field(strict=True)],
        shop_id: Optional[StrictInt] = None,
    ) -> OR72Response200:
        """List the documents on orders (OR72)."""
        return await self._call(
            _o_r72,
            order_ids=order_ids,
            shop_id=shop_id,
        )

    @checked
    async def download_documents(
        self,
        *,
        order_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        document_ids: Optional[Annotated[str, Field(strict=True)]] = None,
        document_codes: Optional[Annotated[str, Field(strict=True)]] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download one or more order documents (OR73). Close the download, or read it in an `async with` block."""
        return await self._download(
            _o_r73,
            order_ids=order_ids,
            document_ids=document_ids,
            document_codes=document_codes,
            shop_id=shop_id,
        )

    @checked
    async def upload_documents(
        self,
        order_id: StrictStr,
        *,
        files: List[FileInput],
        order_documents: OR74RequestMultipartFormDataOrderDocuments,
        shop_id: Optional[StrictInt] = None,
    ) -> OR74Response200:
        """Upload documents to an order (OR74)."""
        return await self._call(
            _o_r74,
            order_id=order_id,
            shop_id=shop_id,
            files=files,
            order_documents=order_documents,
        )

    @checked
    async def list_taxes(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> OR75Response200:
        """List the order taxes the platform uses (OR75)."""
        return await self._call(
            _o_r75,
            shop_id=shop_id,
        )

    @checked
    async def delete_document(
        self,
        document_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Delete an order document (OR76)."""
        return await self._call(
            _o_r76,
            document_id=document_id,
            shop_id=shop_id,
        )
