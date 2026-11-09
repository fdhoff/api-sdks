# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.post_order.models.appeal_request import AppealRequest
from ebay_sell.post_order.models.case_details_response import CaseDetailsResponse
from ebay_sell.post_order.models.case_search_response import CaseSearchResponse

_appeal_case_decision: Operation[None] = Operation(
    id="appealCaseDecision",
    method="POST",
    path="/post-order/v2/casemanagement/{caseId}/appeal",
    resource="cases",
    name="appeal",
    params=(
        Param("caseId", "case_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=None,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_get_case: Operation[CaseDetailsResponse] = Operation(
    id="getCase",
    method="GET",
    path="/post-order/v2/casemanagement/{caseId}",
    resource="cases",
    name="get",
    params=(
        Param("caseId", "case_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=CaseDetailsResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)
_search_cases: Operation[CaseSearchResponse] = Operation(
    id="searchCases",
    method="GET",
    path="/post-order/v2/casemanagement/search",
    resource="cases",
    name="search",
    params=(
        Param("case_creation_date_range_from", "case_creation_date_range_from", "query"),
        Param("case_creation_date_range_to", "case_creation_date_range_to", "query"),
        Param("case_status_filter", "case_status_filter", "query"),
        Param("fieldgroups", "fieldgroups", "query"),
        Param("item_id", "item_id", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("order_id", "order_id", "query"),
        Param("return_id", "return_id", "query"),
        Param("sort", "sort", "query"),
        Param("transaction_id", "transaction_id", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=CaseSearchResponse,
    returns_json=True,
    security=((Scheme("api_auth", ()),),),
    host="api",
)

OPERATIONS = (
    _appeal_case_decision,
    _get_case,
    _search_cases,
)


class CasesApi(Resource):
    @checked
    def appeal(
        self,
        case_id: StrictStr,
        body: Optional[Union[AppealRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Appeal the decision on a case."""
        return self._call(
            _appeal_case_decision,
            case_id=case_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get(
        self,
        case_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> CaseDetailsResponse:
        """Get one case."""
        return self._call(
            _get_case,
            case_id=case_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        case_creation_date_range_from: Optional[StrictStr] = None,
        case_creation_date_range_to: Optional[StrictStr] = None,
        case_status_filter: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_id: Optional[StrictStr] = None,
        return_id: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> CaseSearchResponse:
        """Search one page of cases."""
        return self._call(
            _search_cases,
            case_creation_date_range_from=case_creation_date_range_from,
            case_creation_date_range_to=case_creation_date_range_to,
            case_status_filter=case_status_filter,
            fieldgroups=fieldgroups,
            item_id=item_id,
            limit=limit,
            offset=offset,
            order_id=order_id,
            return_id=return_id,
            sort=sort,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncCasesApi(AsyncResource):
    @checked
    async def appeal(
        self,
        case_id: StrictStr,
        body: Optional[Union[AppealRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Appeal the decision on a case."""
        return await self._call(
            _appeal_case_decision,
            case_id=case_id,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get(
        self,
        case_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> CaseDetailsResponse:
        """Get one case."""
        return await self._call(
            _get_case,
            case_id=case_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def search(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        case_creation_date_range_from: Optional[StrictStr] = None,
        case_creation_date_range_to: Optional[StrictStr] = None,
        case_status_filter: Optional[StrictStr] = None,
        fieldgroups: Optional[StrictStr] = None,
        item_id: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_id: Optional[StrictStr] = None,
        return_id: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> CaseSearchResponse:
        """Search one page of cases."""
        return await self._call(
            _search_cases,
            case_creation_date_range_from=case_creation_date_range_from,
            case_creation_date_range_to=case_creation_date_range_to,
            case_status_filter=case_status_filter,
            fieldgroups=fieldgroups,
            item_id=item_id,
            limit=limit,
            offset=offset,
            order_id=order_id,
            return_id=return_id,
            sort=sort,
            transaction_id=transaction_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
