# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.payment_account_ledger_entries import PaymentAccountLedgerEntries
from etsy_seller.models.payment_account_ledger_entry import PaymentAccountLedgerEntry

_get_shop_payment_account_ledger_entries: Operation[PaymentAccountLedgerEntries] = Operation(
    id="getShopPaymentAccountLedgerEntries",
    method="GET",
    path="/v3/application/shops/{shop_id}/payment-account/ledger-entries",
    resource="ledger_entries",
    name="list",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("min_created", "min_created", "query"),
        Param("max_created", "max_created", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=PaymentAccountLedgerEntries,
    returns_json=True,
    iterator="iter",
    item=_models.PaymentAccountLedgerEntry,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_shop_payment_account_ledger_entry: Operation[PaymentAccountLedgerEntry] = Operation(
    id="getShopPaymentAccountLedgerEntry",
    method="GET",
    path="/v3/application/shops/{shop_id}/payment-account/ledger-entries/{ledger_entry_id}",
    resource="ledger_entries",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("ledger_entry_id", "ledger_entry_id", "path"),
    ),
    response=PaymentAccountLedgerEntry,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)

OPERATIONS = (
    _get_shop_payment_account_ledger_entries,
    _get_shop_payment_account_ledger_entry,
)


class LedgerEntriesApi(Resource):
    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Annotated[int, Field(strict=True, ge=946684800)],
        max_created: Annotated[int, Field(strict=True, ge=946684800)],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> PaymentAccountLedgerEntries:
        """List one page of a shop&#39;s payment account ledger entries."""
        return self._call(
            _get_shop_payment_account_ledger_entries,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Annotated[int, Field(strict=True, ge=946684800)],
        max_created: Annotated[int, Field(strict=True, ge=946684800)],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.PaymentAccountLedgerEntry]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_payment_account_ledger_entries,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            limit=limit,
            offset=offset,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        ledger_entry_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> PaymentAccountLedgerEntry:
        """Get one payment account ledger entry."""
        return self._call(
            _get_shop_payment_account_ledger_entry,
            shop_id=shop_id,
            ledger_entry_id=ledger_entry_id,
        )


class AsyncLedgerEntriesApi(AsyncResource):
    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Annotated[int, Field(strict=True, ge=946684800)],
        max_created: Annotated[int, Field(strict=True, ge=946684800)],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> PaymentAccountLedgerEntries:
        """List one page of a shop&#39;s payment account ledger entries."""
        return await self._call(
            _get_shop_payment_account_ledger_entries,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        min_created: Annotated[int, Field(strict=True, ge=946684800)],
        max_created: Annotated[int, Field(strict=True, ge=946684800)],
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.PaymentAccountLedgerEntry]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_payment_account_ledger_entries,
            shop_id=shop_id,
            min_created=min_created,
            max_created=max_created,
            limit=limit,
            offset=offset,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        ledger_entry_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> PaymentAccountLedgerEntry:
        """Get one payment account ledger entry."""
        return await self._call(
            _get_shop_payment_account_ledger_entry,
            shop_id=shop_id,
            ledger_entry_id=ledger_entry_id,
        )
