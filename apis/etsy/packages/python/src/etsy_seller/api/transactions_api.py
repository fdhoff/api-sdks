# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import Field, StrictBool
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_receipt_transaction import ShopReceiptTransaction
from etsy_seller.models.shop_receipt_transactions import ShopReceiptTransactions

_get_shop_receipt_transaction: Operation[ShopReceiptTransaction] = Operation(
    id="getShopReceiptTransaction",
    method="GET",
    path="/v3/application/shops/{shop_id}/transactions/{transaction_id}",
    resource="transactions",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("transaction_id", "transaction_id", "path"),
    ),
    response=ShopReceiptTransaction,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_shop_receipt_transactions_by_listing: Operation[ShopReceiptTransactions] = Operation(
    id="getShopReceiptTransactionsByListing",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/transactions",
    resource="transactions",
    name="list_by_listing",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopReceiptTransactions,
    returns_json=True,
    iterator="iter_by_listing",
    item=_models.ShopReceiptTransaction,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_shop_receipt_transactions_by_receipt: Operation[ShopReceiptTransactions] = Operation(
    id="getShopReceiptTransactionsByReceipt",
    method="GET",
    path="/v3/application/shops/{shop_id}/receipts/{receipt_id}/transactions",
    resource="transactions",
    name="list_by_receipt",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("receipt_id", "receipt_id", "path"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopReceiptTransactions,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_shop_receipt_transactions_by_shop: Operation[ShopReceiptTransactions] = Operation(
    id="getShopReceiptTransactionsByShop",
    method="GET",
    path="/v3/application/shops/{shop_id}/transactions",
    resource="transactions",
    name="list",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("legacy", "legacy", "query"),
    ),
    response=ShopReceiptTransactions,
    returns_json=True,
    iterator="iter",
    item=_models.ShopReceiptTransaction,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)

OPERATIONS = (
    _get_shop_receipt_transaction,
    _get_shop_receipt_transactions_by_listing,
    _get_shop_receipt_transactions_by_receipt,
    _get_shop_receipt_transactions_by_shop,
)


class TransactionsApi(Resource):
    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        transaction_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReceiptTransaction:
        """Get one transaction."""
        return self._call(
            _get_shop_receipt_transaction,
            shop_id=shop_id,
            transaction_id=transaction_id,
        )

    @checked
    def list_by_listing(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceiptTransactions:
        """List one page of a listing&#39;s transactions."""
        return self._call(
            _get_shop_receipt_transactions_by_listing,
            shop_id=shop_id,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter_by_listing(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> Iterator[_models.ShopReceiptTransaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_receipt_transactions_by_listing,
            shop_id=shop_id,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def list_by_receipt(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceiptTransactions:
        """List the transactions on a receipt."""
        return self._call(
            _get_shop_receipt_transactions_by_receipt,
            shop_id=shop_id,
            receipt_id=receipt_id,
            legacy=legacy,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceiptTransactions:
        """List one page of a shop&#39;s transactions."""
        return self._call(
            _get_shop_receipt_transactions_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> Iterator[_models.ShopReceiptTransaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_receipt_transactions_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )


class AsyncTransactionsApi(AsyncResource):
    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        transaction_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopReceiptTransaction:
        """Get one transaction."""
        return await self._call(
            _get_shop_receipt_transaction,
            shop_id=shop_id,
            transaction_id=transaction_id,
        )

    @checked
    async def list_by_listing(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceiptTransactions:
        """List one page of a listing&#39;s transactions."""
        return await self._call(
            _get_shop_receipt_transactions_by_listing,
            shop_id=shop_id,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter_by_listing(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.ShopReceiptTransaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_receipt_transactions_by_listing,
            shop_id=shop_id,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    async def list_by_receipt(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceiptTransactions:
        """List the transactions on a receipt."""
        return await self._call(
            _get_shop_receipt_transactions_by_receipt,
            shop_id=shop_id,
            receipt_id=receipt_id,
            legacy=legacy,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> ShopReceiptTransactions:
        """List one page of a shop&#39;s transactions."""
        return await self._call(
            _get_shop_receipt_transactions_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        legacy: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.ShopReceiptTransaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_receipt_transactions_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            legacy=legacy,
        )
