# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.post_order.models.create_return_request import CreateReturnRequest
from ebay_sell.post_order.models.create_return_response import CreateReturnResponse
from ebay_sell.post_order.models.decide_return_request import DecideReturnRequest
from ebay_sell.post_order.models.decide_return_response import DecideReturnResponse
from ebay_sell.post_order.models.escalate_request import EscalateRequest
from ebay_sell.post_order.models.escalate_response import EscalateResponse
from ebay_sell.post_order.models.get_detail_response import GetDetailResponse
from ebay_sell.post_order.models.get_file_response import GetFileResponse
from ebay_sell.post_order.models.get_summary_response import GetSummaryResponse
from ebay_sell.post_order.models.get_tracking_history_response import GetTrackingHistoryResponse
from ebay_sell.post_order.models.issue_refund_request import IssueRefundRequest
from ebay_sell.post_order.models.issue_refund_response import IssueRefundResponse
from ebay_sell.post_order.models.mark_as_received_request import MarkAsReceivedRequest
from ebay_sell.post_order.models.provide_label_request import ProvideLabelRequest
from ebay_sell.post_order.models.provide_label_response import ProvideLabelResponse
from ebay_sell.post_order.models.send_message_request import SendMessageRequest
from ebay_sell.post_order.models.upload_file_request import UploadFileRequest
from ebay_sell.post_order.models.upload_file_response import UploadFileResponse

_add_shipping_label_info: Operation[ProvideLabelResponse] = Operation(
    id="addShippingLabelInfo",
    method="POST",
    path="/post-order/v2/return/{returnId}/add_shipping_label",
    resource="returns",
    name="add_shipping_label",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=ProvideLabelResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_create_return_request: Operation[CreateReturnResponse] = Operation(
    id="createReturnRequest",
    method="POST",
    path="/post-order/v2/return",
    resource="returns",
    name="create",
    params=(
        Param("fieldgroups", "fieldgroups", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=CreateReturnResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_escalate_return: Operation[EscalateResponse] = Operation(
    id="escalateReturn",
    method="POST",
    path="/post-order/v2/return/{returnId}/escalate",
    resource="returns",
    name="escalate",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=EscalateResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_get_return: Operation[GetDetailResponse] = Operation(
    id="getReturn",
    method="GET",
    path="/post-order/v2/return/{returnId}",
    resource="returns",
    name="get",
    params=(
        Param("returnId", "return_id", "path"),
        Param("fieldgroups", "fieldgroups", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=GetDetailResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_get_return_files: Operation[GetFileResponse] = Operation(
    id="getReturnFiles",
    method="GET",
    path="/post-order/v2/return/{returnId}/files",
    resource="returns",
    name="list_files",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=GetFileResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_get_shipment_tracking_info: Operation[GetTrackingHistoryResponse] = Operation(
    id="getShipmentTrackingInfo",
    method="GET",
    path="/post-order/v2/return/{returnId}/tracking",
    resource="returns",
    name="get_tracking",
    params=(
        Param("returnId", "return_id", "path"),
        Param("carrier_used", "carrier_used", "query"),
        Param("tracking_number", "tracking_number", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=GetTrackingHistoryResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_issue_return_refund: Operation[IssueRefundResponse] = Operation(
    id="issueReturnRefund",
    method="POST",
    path="/post-order/v2/return/{returnId}/issue_refund",
    resource="returns",
    name="issue_refund",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=IssueRefundResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_mark_item_received: Operation[object] = Operation(
    id="markItemReceived",
    method="POST",
    path="/post-order/v2/return/{returnId}/mark_as_received",
    resource="returns",
    name="mark_received",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_process_return_request: Operation[DecideReturnResponse] = Operation(
    id="processReturnRequest",
    method="POST",
    path="/post-order/v2/return/{returnId}/decide",
    resource="returns",
    name="decide",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=DecideReturnResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_search_returns: Operation[GetSummaryResponse] = Operation(
    id="searchReturns",
    method="GET",
    path="/post-order/v2/return/search",
    resource="returns",
    name="search",
    params=(
        Param("creation_date_range_from", "creation_date_range_from", "query"),
        Param("creation_date_range_to", "creation_date_range_to", "query"),
        Param("item_id", "item_id", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("order_id", "order_id", "query"),
        Param("return_id", "return_id", "query"),
        Param("return_state", "return_state", "query"),
        Param("role", "role", "query"),
        Param("sort", "sort", "query"),
        Param("states", "states", "query"),
        Param("transaction_id", "transaction_id", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=GetSummaryResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_send_return_message: Operation[object] = Operation(
    id="sendReturnMessage",
    method="POST",
    path="/post-order/v2/return/{returnId}/send_message",
    resource="returns",
    name="send_message",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_upload_return_file: Operation[UploadFileResponse] = Operation(
    id="uploadReturnFile",
    method="POST",
    path="/post-order/v2/return/{returnId}/file/upload",
    resource="returns",
    name="upload_file",
    params=(
        Param("returnId", "return_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=UploadFileResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)

OPERATIONS = (
    _add_shipping_label_info,
    _create_return_request,
    _escalate_return,
    _get_return,
    _get_return_files,
    _get_shipment_tracking_info,
    _issue_return_refund,
    _mark_item_received,
    _process_return_request,
    _search_returns,
    _send_return_message,
    _upload_return_file,
)


class ReturnsApi(Resource):
    @checked
    def add_shipping_label(
        self,
        return_id: StrictStr,
        body: Union[ProvideLabelRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> ProvideLabelResponse:
        """Give the buyer a return shipping label, or say why there is none."""
        return self._call(
            _add_shipping_label_info,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def create(
        self,
        body: Union[CreateReturnRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
    ) -> CreateReturnResponse:
        """Create a return request."""
        return self._call(
            _create_return_request,
            _body=body,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def escalate(
        self,
        return_id: StrictStr,
        body: Union[EscalateRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> EscalateResponse:
        """Escalate a return request to a case."""
        return self._call(
            _escalate_return,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get(
        self,
        return_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
    ) -> GetDetailResponse:
        """Get one return request."""
        return self._call(
            _get_return,
            return_id=return_id,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def list_files(
        self,
        return_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetFileResponse:
        """List the files attached to a return request."""
        return self._call(
            _get_return_files,
            return_id=return_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get_tracking(
        self,
        return_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        carrier_used: Optional[StrictStr] = None,
        tracking_number: Optional[StrictStr] = None,
    ) -> GetTrackingHistoryResponse:
        """Get the tracking of a return shipment."""
        return self._call(
            _get_shipment_tracking_info,
            return_id=return_id,
            carrier_used=carrier_used,
            tracking_number=tracking_number,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def issue_refund(
        self,
        return_id: StrictStr,
        body: Union[IssueRefundRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> IssueRefundResponse:
        """Refund the buyer for a return."""
        return self._call(
            _issue_return_refund,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def mark_received(
        self,
        return_id: StrictStr,
        body: Optional[Union[MarkAsReceivedRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Mark a returned item received."""
        return self._call(
            _mark_item_received,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def decide(
        self,
        return_id: StrictStr,
        body: Union[DecideReturnRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> DecideReturnResponse:
        """Accept or decline a return request, or offer a partial refund."""
        return self._call(
            _process_return_request,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        creation_date_range_from: Optional[StrictStr] = None,
        creation_date_range_to: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_id: Optional[StrictStr] = None,
        return_id: Optional[StrictStr] = None,
        return_state: Optional[StrictStr] = None,
        role: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        states: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> GetSummaryResponse:
        """Search one page of return requests."""
        return self._call(
            _search_returns,
            creation_date_range_from=creation_date_range_from,
            creation_date_range_to=creation_date_range_to,
            item_id=item_id,
            limit=limit,
            offset=offset,
            order_id=order_id,
            return_id=return_id,
            return_state=return_state,
            role=role,
            sort=sort,
            states=states,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def send_message(
        self,
        return_id: StrictStr,
        body: Union[SendMessageRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Send the buyer a message about a return."""
        return self._call(
            _send_return_message,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def upload_file(
        self,
        return_id: StrictStr,
        body: Union[UploadFileRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> UploadFileResponse:
        """Attach a base64-encoded file to a return request."""
        return self._call(
            _upload_return_file,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncReturnsApi(AsyncResource):
    @checked
    async def add_shipping_label(
        self,
        return_id: StrictStr,
        body: Union[ProvideLabelRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> ProvideLabelResponse:
        """Give the buyer a return shipping label, or say why there is none."""
        return await self._call(
            _add_shipping_label_info,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def create(
        self,
        body: Union[CreateReturnRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
    ) -> CreateReturnResponse:
        """Create a return request."""
        return await self._call(
            _create_return_request,
            _body=body,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def escalate(
        self,
        return_id: StrictStr,
        body: Union[EscalateRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> EscalateResponse:
        """Escalate a return request to a case."""
        return await self._call(
            _escalate_return,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get(
        self,
        return_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
    ) -> GetDetailResponse:
        """Get one return request."""
        return await self._call(
            _get_return,
            return_id=return_id,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def list_files(
        self,
        return_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> GetFileResponse:
        """List the files attached to a return request."""
        return await self._call(
            _get_return_files,
            return_id=return_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get_tracking(
        self,
        return_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        carrier_used: Optional[StrictStr] = None,
        tracking_number: Optional[StrictStr] = None,
    ) -> GetTrackingHistoryResponse:
        """Get the tracking of a return shipment."""
        return await self._call(
            _get_shipment_tracking_info,
            return_id=return_id,
            carrier_used=carrier_used,
            tracking_number=tracking_number,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def issue_refund(
        self,
        return_id: StrictStr,
        body: Union[IssueRefundRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> IssueRefundResponse:
        """Refund the buyer for a return."""
        return await self._call(
            _issue_return_refund,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def mark_received(
        self,
        return_id: StrictStr,
        body: Optional[Union[MarkAsReceivedRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Mark a returned item received."""
        return await self._call(
            _mark_item_received,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def decide(
        self,
        return_id: StrictStr,
        body: Union[DecideReturnRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> DecideReturnResponse:
        """Accept or decline a return request, or offer a partial refund."""
        return await self._call(
            _process_return_request,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        creation_date_range_from: Optional[StrictStr] = None,
        creation_date_range_to: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_id: Optional[StrictStr] = None,
        return_id: Optional[StrictStr] = None,
        return_state: Optional[StrictStr] = None,
        role: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        states: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> GetSummaryResponse:
        """Search one page of return requests."""
        return await self._call(
            _search_returns,
            creation_date_range_from=creation_date_range_from,
            creation_date_range_to=creation_date_range_to,
            item_id=item_id,
            limit=limit,
            offset=offset,
            order_id=order_id,
            return_id=return_id,
            return_state=return_state,
            role=role,
            sort=sort,
            states=states,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def send_message(
        self,
        return_id: StrictStr,
        body: Union[SendMessageRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Send the buyer a message about a return."""
        return await self._call(
            _send_return_message,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def upload_file(
        self,
        return_id: StrictStr,
        body: Union[UploadFileRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> UploadFileResponse:
        """Attach a base64-encoded file to a return request."""
        return await self._call(
            _upload_return_file,
            return_id=return_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
