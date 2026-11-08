# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import List

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.payments import Payments

_get_payment_account_ledger_entry_payments: Operation[Payments] = Operation(
    id="getPaymentAccountLedgerEntryPayments",
    method="GET",
    path="/v3/application/shops/{shop_id}/payment-account/ledger-entries/payments",
    resource="payments",
    name="list_by_ledger_entries",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("ledger_entry_ids", "ledger_entry_ids", "query"),
    ),
    response=Payments,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_payments: Operation[Payments] = Operation(
    id="getPayments",
    method="GET",
    path="/v3/application/shops/{shop_id}/payments",
    resource="payments",
    name="list",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("payment_ids", "payment_ids", "query"),
    ),
    response=Payments,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)
_get_shop_payment_by_receipt_id: Operation[Payments] = Operation(
    id="getShopPaymentByReceiptId",
    method="GET",
    path="/v3/application/shops/{shop_id}/receipts/{receipt_id}/payments",
    resource="payments",
    name="list_by_receipt",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("receipt_id", "receipt_id", "path"),
    ),
    response=Payments,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("transactions_r",)),
        ),
    ),
)

OPERATIONS = (
    _get_payment_account_ledger_entry_payments,
    _get_payments,
    _get_shop_payment_by_receipt_id,
)


class PaymentsApi(Resource):
    @checked
    def list_by_ledger_entries(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        ledger_entry_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> Payments:
        """Get the payments behind several ledger entries."""
        return self._call(
            _get_payment_account_ledger_entry_payments,
            shop_id=shop_id,
            ledger_entry_ids=ledger_entry_ids,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        payment_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> Payments:
        """Get several payments by ID."""
        return self._call(
            _get_payments,
            shop_id=shop_id,
            payment_ids=payment_ids,
        )

    @checked
    def list_by_receipt(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> Payments:
        """List the payments for a receipt."""
        return self._call(
            _get_shop_payment_by_receipt_id,
            shop_id=shop_id,
            receipt_id=receipt_id,
        )


class AsyncPaymentsApi(AsyncResource):
    @checked
    async def list_by_ledger_entries(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        ledger_entry_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> Payments:
        """Get the payments behind several ledger entries."""
        return await self._call(
            _get_payment_account_ledger_entry_payments,
            shop_id=shop_id,
            ledger_entry_ids=ledger_entry_ids,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        payment_ids: List[Annotated[int, Field(strict=True, ge=1)]],
    ) -> Payments:
        """Get several payments by ID."""
        return await self._call(
            _get_payments,
            shop_id=shop_id,
            payment_ids=payment_ids,
        )

    @checked
    async def list_by_receipt(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        receipt_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> Payments:
        """List the payments for a receipt."""
        return await self._call(
            _get_shop_payment_by_receipt_id,
            shop_id=shop_id,
            receipt_id=receipt_id,
        )
