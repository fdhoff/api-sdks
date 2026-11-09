# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.post_order.models.create_cancel_request import CreateCancelRequest
from ebay_sell.post_order.models.create_cancel_response import CreateCancelResponse
from ebay_sell.post_order.models.find_cancel_response import FindCancelResponse
from ebay_sell.post_order.models.get_cancel_detail_response import GetCancelDetailResponse
from ebay_sell.post_order.models.order_eligibility_check_info import OrderEligibilityCheckInfo
from ebay_sell.post_order.models.order_eligibility_result import OrderEligibilityResult
from ebay_sell.post_order.models.reject_cancel_request import RejectCancelRequest

_approve_cancellation: Operation[object] = Operation(
    id="approveCancellation",
    method="POST",
    path="/post-order/v2/cancellation/{cancelId}/approve",
    resource="cancellations",
    name="approve",
    params=(
        Param("cancelId", "cancel_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_check_cancellation_eligibility: Operation[OrderEligibilityResult] = Operation(
    id="checkCancellationEligibility",
    method="POST",
    path="/post-order/v2/cancellation/check_eligibility",
    resource="cancellations",
    name="check_eligibility",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=OrderEligibilityResult,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_create_cancellation_request: Operation[CreateCancelResponse] = Operation(
    id="createCancellationRequest",
    method="POST",
    path="/post-order/v2/cancellation",
    resource="cancellations",
    name="create",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=CreateCancelResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_get_cancellation: Operation[GetCancelDetailResponse] = Operation(
    id="getCancellation",
    method="GET",
    path="/post-order/v2/cancellation/{cancelId}",
    resource="cancellations",
    name="get",
    params=(
        Param("cancelId", "cancel_id", "path"),
        Param("fieldgroups", "fieldgroups", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=GetCancelDetailResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_reject_cancellation: Operation[object] = Operation(
    id="rejectCancellation",
    method="POST",
    path="/post-order/v2/cancellation/{cancelId}/reject",
    resource="cancellations",
    name="reject",
    params=(
        Param("cancelId", "cancel_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_search_cancellations: Operation[FindCancelResponse] = Operation(
    id="searchCancellations",
    method="GET",
    path="/post-order/v2/cancellation/search",
    resource="cancellations",
    name="search",
    params=(
        Param("cancel_id", "cancel_id", "query"),
        Param("creation_date_range_from", "creation_date_range_from", "query"),
        Param("creation_date_range_to", "creation_date_range_to", "query"),
        Param("item_id", "item_id", "query"),
        Param("legacy_order_id", "legacy_order_id", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("role", "role", "query"),
        Param("sort", "sort", "query"),
        Param("transaction_id", "transaction_id", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=FindCancelResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)

OPERATIONS = (
    _approve_cancellation,
    _check_cancellation_eligibility,
    _create_cancellation_request,
    _get_cancellation,
    _reject_cancellation,
    _search_cancellations,
)


class CancellationsApi(Resource):
    @checked
    def approve(
        self,
        cancel_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Approve a buyer's cancellation request."""
        return self._call(
            _approve_cancellation,
            cancel_id=cancel_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def check_eligibility(
        self,
        body: Union[OrderEligibilityCheckInfo, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> OrderEligibilityResult:
        """Check whether an order can be cancelled."""
        return self._call(
            _check_cancellation_eligibility,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def create(
        self,
        body: Union[CreateCancelRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> CreateCancelResponse:
        """Ask to cancel an order."""
        return self._call(
            _create_cancellation_request,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get(
        self,
        cancel_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
    ) -> GetCancelDetailResponse:
        """Get one cancellation request."""
        return self._call(
            _get_cancellation,
            cancel_id=cancel_id,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def reject(
        self,
        cancel_id: StrictStr,
        body: Optional[Union[RejectCancelRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Reject a buyer's cancellation request."""
        return self._call(
            _reject_cancellation,
            cancel_id=cancel_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        cancel_id: Optional[StrictStr] = None,
        creation_date_range_from: Optional[StrictStr] = None,
        creation_date_range_to: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        legacy_order_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        role: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> FindCancelResponse:
        """Search one page of cancellation requests."""
        return self._call(
            _search_cancellations,
            cancel_id=cancel_id,
            creation_date_range_from=creation_date_range_from,
            creation_date_range_to=creation_date_range_to,
            item_id=item_id,
            legacy_order_id=legacy_order_id,
            limit=limit,
            offset=offset,
            role=role,
            sort=sort,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncCancellationsApi(AsyncResource):
    @checked
    async def approve(
        self,
        cancel_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Approve a buyer's cancellation request."""
        return await self._call(
            _approve_cancellation,
            cancel_id=cancel_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def check_eligibility(
        self,
        body: Union[OrderEligibilityCheckInfo, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> OrderEligibilityResult:
        """Check whether an order can be cancelled."""
        return await self._call(
            _check_cancellation_eligibility,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def create(
        self,
        body: Union[CreateCancelRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> CreateCancelResponse:
        """Ask to cancel an order."""
        return await self._call(
            _create_cancellation_request,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get(
        self,
        cancel_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
    ) -> GetCancelDetailResponse:
        """Get one cancellation request."""
        return await self._call(
            _get_cancellation,
            cancel_id=cancel_id,
            fieldgroups=fieldgroups,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def reject(
        self,
        cancel_id: StrictStr,
        body: Optional[Union[RejectCancelRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> object:
        """Reject a buyer's cancellation request."""
        return await self._call(
            _reject_cancellation,
            cancel_id=cancel_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        cancel_id: Optional[StrictStr] = None,
        creation_date_range_from: Optional[StrictStr] = None,
        creation_date_range_to: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        legacy_order_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        role: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> FindCancelResponse:
        """Search one page of cancellation requests."""
        return await self._call(
            _search_cancellations,
            cancel_id=cancel_id,
            creation_date_range_from=creation_date_range_from,
            creation_date_range_to=creation_date_range_to,
            item_id=item_id,
            legacy_order_id=legacy_order_id,
            limit=limit,
            offset=offset,
            role=role,
            sort=sort,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
