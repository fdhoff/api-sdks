# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.iv01_response200_invoices import IV01Response200Invoices
from mirakl_seller.models.iv01_response200_invoices_auto_invoice_payment_info import (
    IV01Response200InvoicesAutoInvoicePaymentInfo,
)
from mirakl_seller.models.iv01_response200_invoices_auto_invoice_summary import (
    IV01Response200InvoicesAutoInvoiceSummary,
)
from mirakl_seller.models.iv01_response200_invoices_details import IV01Response200InvoicesDetails
from mirakl_seller.models.iv01_response200_invoices_issuing_user import IV01Response200InvoicesIssuingUser
from mirakl_seller.models.iv01_response200_invoices_payment import IV01Response200InvoicesPayment
from mirakl_seller.models.iv01_response200_invoices_shop_address import IV01Response200InvoicesShopAddress
from mirakl_seller.models.iv01_response200_invoices_total_taxes import IV01Response200InvoicesTotalTaxes
from mirakl_seller._runtime import ApiModel


class IV01Response200InvoicesAutoInvoice(IV01Response200Invoices):
    """IV01Response200InvoicesAutoInvoice model."""

    end_time: Optional[datetime] = None
    payment_info: Optional[IV01Response200InvoicesAutoInvoicePaymentInfo] = None
    seller_billing_cycle_id: Optional[StrictStr] = None
    start_time: Optional[datetime] = None
    summary: Optional[IV01Response200InvoicesAutoInvoiceSummary] = None
