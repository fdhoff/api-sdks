# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.finances import models as _models
from ebay_sell.finances.models.transaction_summary_response import TransactionSummaryResponse
from ebay_sell.finances.models.transactions import Transactions

_get_transaction_summary: Operation[TransactionSummaryResponse] = Operation(
    id="getTransactionSummary",
    method="GET",
    path="/sell/finances/v1/transaction_summary",
    resource="transactions",
    name="get_summary",
    params=(
        Param("filter", "filter", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=TransactionSummaryResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="apiz",
)
_get_transactions: Operation[Transactions] = Operation(
    id="getTransactions",
    method="GET",
    path="/sell/finances/v1/transaction",
    resource="transactions",
    name="list",
    params=(
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=Transactions,
    returns_json=True,
    iterator="iter",
    item=_models.Transaction,
    paging=NextLink(
        items="transactions",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="apiz",
)

OPERATIONS = (
    _get_transaction_summary,
    _get_transactions,
)


class TransactionsApi(Resource):
    @checked
    def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
    ) -> TransactionSummaryResponse:
        """Sum the seller's monetary transactions by type."""
        return self._call(
            _get_transaction_summary,
            filter=filter,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def list(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Transactions:
        """List one page of the seller's monetary transactions."""
        return self._call(
            _get_transactions,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.Transaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_transactions,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncTransactionsApi(AsyncResource):
    @checked
    async def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
    ) -> TransactionSummaryResponse:
        """Sum the seller's monetary transactions by type."""
        return await self._call(
            _get_transaction_summary,
            filter=filter,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def list(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Transactions:
        """List one page of the seller's monetary transactions."""
        return await self._call(
            _get_transactions,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Transaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_transactions,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
