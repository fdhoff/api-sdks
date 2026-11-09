# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from mirakl_seller.models.iv01_response200_invoices_details import IV01Response200InvoicesDetails
from mirakl_seller.models.iv01_response200_invoices_issuing_user import IV01Response200InvoicesIssuingUser
from mirakl_seller.models.iv01_response200_invoices_payment import IV01Response200InvoicesPayment
from mirakl_seller.models.iv01_response200_invoices_shop_address import IV01Response200InvoicesShopAddress
from mirakl_seller.models.iv01_response200_invoices_total_taxes import IV01Response200InvoicesTotalTaxes
from mirakl_seller._runtime import ApiModel


class IV01Response200Invoices(ApiModel):
    """IV01Response200Invoices model."""

    currency_iso_code: Optional[StrictStr] = None
    date_created: Optional[datetime] = None
    details: Optional[List[IV01Response200InvoicesDetails]] = None
    due_date: Optional[datetime] = None
    id: Optional[StrictStr] = None
    invoice_id: Optional[StrictInt] = None
    issue_date: Optional[datetime] = None
    issuing_user: Optional[IV01Response200InvoicesIssuingUser] = None
    pay_out_psp_code: Optional[StrictStr] = None
    payment: Optional[IV01Response200InvoicesPayment] = None
    shop_address: Optional[IV01Response200InvoicesShopAddress] = None
    shop_corporate_name: Optional[StrictStr] = None
    shop_id: Optional[StrictInt] = None
    shop_model: Optional[StrictStr] = None
    shop_name: Optional[StrictStr] = None
    shop_operator_internal_id: Optional[StrictStr] = None
    shop_tax_number: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    total_amount_excl_taxes: Optional[float] = None
    total_amount_incl_taxes: Optional[float] = None
    total_charged_amount: Optional[float] = None
    total_taxes: Optional[List[IV01Response200InvoicesTotalTaxes]] = None
    type: Optional[StrictStr] = None
