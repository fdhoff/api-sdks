# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.iv01_response200_invoices_auto_invoice_payment_info import (
    IV01Response200InvoicesAutoInvoicePaymentInfo,
)
from mirakl_seller._runtime import ApiModel


class IV01Response200InvoicesAutoInvoicePaymentInfoPayout(IV01Response200InvoicesAutoInvoicePaymentInfo):
    """IV01Response200InvoicesAutoInvoicePaymentInfoPayout model."""

    bank_account_number: Optional[StrictStr] = None
    bic: Optional[StrictStr] = None
    iban: Optional[StrictStr] = None
    payout_format: Optional[StrictStr] = None
    sort_code: Optional[StrictStr] = None
