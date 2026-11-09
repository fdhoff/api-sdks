# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.iv01_response200_invoices import IV01Response200Invoices
from mirakl_seller.models.iv01_response200_invoices_details import IV01Response200InvoicesDetails
from mirakl_seller.models.iv01_response200_invoices_issuing_user import IV01Response200InvoicesIssuingUser
from mirakl_seller.models.iv01_response200_invoices_payment import IV01Response200InvoicesPayment
from mirakl_seller.models.iv01_response200_invoices_shop_address import IV01Response200InvoicesShopAddress
from mirakl_seller.models.iv01_response200_invoices_total_taxes import IV01Response200InvoicesTotalTaxes
from mirakl_seller._runtime import ApiModel


class IV01Response200InvoicesManualCredit(IV01Response200Invoices):
    """IV01Response200InvoicesManualCredit model."""

    emission_date: Optional[datetime] = None
    seller_billing_cycle_id: Optional[StrictStr] = None
