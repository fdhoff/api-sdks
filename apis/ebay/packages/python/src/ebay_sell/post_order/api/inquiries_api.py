# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.post_order.models.escalate_inquiry_request import EscalateInquiryRequest
from ebay_sell.post_order.models.inquiry_details_response import InquiryDetailsResponse
from ebay_sell.post_order.models.inquiry_search_response import InquirySearchResponse
from ebay_sell.post_order.models.inquiry_voluntary_refund_request import InquiryVoluntaryRefundRequest
from ebay_sell.post_order.models.send_message_request import SendMessageRequest
from ebay_sell.post_order.models.shipment_info_request import ShipmentInfoRequest
from ebay_sell.post_order.models.voluntary_refund_response import VoluntaryRefundResponse

_escalate_inquiry: Operation[None] = Operation(
    id="escalateInquiry",
    method="POST",
    path="/post-order/v2/inquiry/{inquiryId}/escalate",
    resource="inquiries",
    name="escalate",
    params=(
        Param("inquiryId", "inquiry_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=None,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_get_inquiry: Operation[InquiryDetailsResponse] = Operation(
    id="getInquiry",
    method="GET",
    path="/post-order/v2/inquiry/{inquiryId}",
    resource="inquiries",
    name="get",
    params=(
        Param("inquiryId", "inquiry_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=InquiryDetailsResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_issue_inquiry_refund: Operation[VoluntaryRefundResponse] = Operation(
    id="issueInquiryRefund",
    method="POST",
    path="/post-order/v2/inquiry/{inquiryId}/issue_refund",
    resource="inquiries",
    name="issue_refund",
    params=(
        Param("inquiryId", "inquiry_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=VoluntaryRefundResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_provide_inquiry_shipment_info: Operation[object] = Operation(
    id="provideInquiryShipmentInfo",
    method="POST",
    path="/post-order/v2/inquiry/{inquiryId}/provide_shipment_info",
    resource="inquiries",
    name="provide_shipment_info",
    params=(
        Param("inquiryId", "inquiry_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_search_inquiries: Operation[InquirySearchResponse] = Operation(
    id="searchInquiries",
    method="GET",
    path="/post-order/v2/inquiry/search",
    resource="inquiries",
    name="search",
    params=(
        Param("fieldgroups", "fieldgroups", "query"),
        Param("inquiry_creation_date_range_from", "inquiry_creation_date_range_from", "query"),
        Param("inquiry_creation_date_range_to", "inquiry_creation_date_range_to", "query"),
        Param("inquiry_status", "inquiry_status", "query"),
        Param("item_id", "item_id", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("order_id", "order_id", "query"),
        Param("sort", "sort", "query"),
        Param("transaction_id", "transaction_id", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=InquirySearchResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_send_inquiry_message: Operation[object] = Operation(
    id="sendInquiryMessage",
    method="POST",
    path="/post-order/v2/inquiry/{inquiryId}/send_message",
    resource="inquiries",
    name="send_message",
    params=(
        Param("inquiryId", "inquiry_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)

OPERATIONS = (
    _escalate_inquiry,
    _get_inquiry,
    _issue_inquiry_refund,
    _provide_inquiry_shipment_info,
    _search_inquiries,
    _send_inquiry_message,
)


class InquiriesApi(Resource):
    @checked
    def escalate(
        self,
        inquiry_id: StrictStr,
        body: Union[EscalateInquiryRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Escalate an inquiry to a case."""
        return self._call(
            _escalate_inquiry,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get(
        self,
        inquiry_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> InquiryDetailsResponse:
        """Get one item-not-received inquiry."""
        return self._call(
            _get_inquiry,
            inquiry_id=inquiry_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def issue_refund(
        self,
        inquiry_id: StrictStr,
        body: Optional[Union[InquiryVoluntaryRefundRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> VoluntaryRefundResponse:
        """Refund the buyer to settle an inquiry."""
        return self._call(
            _issue_inquiry_refund,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def provide_shipment_info(
        self,
        inquiry_id: StrictStr,
        body: Union[ShipmentInfoRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Give the shipment tracking for an inquiry."""
        return self._call(
            _provide_inquiry_shipment_info,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
        inquiry_creation_date_range_from: Optional[StrictStr] = None,
        inquiry_creation_date_range_to: Optional[StrictStr] = None,
        inquiry_status: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_id: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> InquirySearchResponse:
        """Search one page of inquiries."""
        return self._call(
            _search_inquiries,
            fieldgroups=fieldgroups,
            inquiry_creation_date_range_from=inquiry_creation_date_range_from,
            inquiry_creation_date_range_to=inquiry_creation_date_range_to,
            inquiry_status=inquiry_status,
            item_id=item_id,
            limit=limit,
            offset=offset,
            order_id=order_id,
            sort=sort,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def send_message(
        self,
        inquiry_id: StrictStr,
        body: Union[SendMessageRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Send the buyer a message about an inquiry."""
        return self._call(
            _send_inquiry_message,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncInquiriesApi(AsyncResource):
    @checked
    async def escalate(
        self,
        inquiry_id: StrictStr,
        body: Union[EscalateInquiryRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Escalate an inquiry to a case."""
        return await self._call(
            _escalate_inquiry,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get(
        self,
        inquiry_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> InquiryDetailsResponse:
        """Get one item-not-received inquiry."""
        return await self._call(
            _get_inquiry,
            inquiry_id=inquiry_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def issue_refund(
        self,
        inquiry_id: StrictStr,
        body: Optional[Union[InquiryVoluntaryRefundRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> VoluntaryRefundResponse:
        """Refund the buyer to settle an inquiry."""
        return await self._call(
            _issue_inquiry_refund,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def provide_shipment_info(
        self,
        inquiry_id: StrictStr,
        body: Union[ShipmentInfoRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Give the shipment tracking for an inquiry."""
        return await self._call(
            _provide_inquiry_shipment_info,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
        inquiry_creation_date_range_from: Optional[StrictStr] = None,
        inquiry_creation_date_range_to: Optional[StrictStr] = None,
        inquiry_status: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_id: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> InquirySearchResponse:
        """Search one page of inquiries."""
        return await self._call(
            _search_inquiries,
            fieldgroups=fieldgroups,
            inquiry_creation_date_range_from=inquiry_creation_date_range_from,
            inquiry_creation_date_range_to=inquiry_creation_date_range_to,
            inquiry_status=inquiry_status,
            item_id=item_id,
            limit=limit,
            offset=offset,
            order_id=order_id,
            sort=sort,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def send_message(
        self,
        inquiry_id: StrictStr,
        body: Union[SendMessageRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Send the buyer a message about an inquiry."""
        return await self._call(
            _send_inquiry_message,
            inquiry_id=inquiry_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
