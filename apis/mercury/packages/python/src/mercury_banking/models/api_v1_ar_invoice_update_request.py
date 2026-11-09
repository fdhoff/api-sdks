# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.api_v1_ar_line_item_data import ApiV1ArLineItemData
from mercury_banking._runtime import ApiModel


class ApiV1ArInvoiceUpdateRequest(ApiModel):
    """ApiV1ArInvoiceUpdateRequest model."""

    ach_debit_enabled: StrictBool = Field(alias="achDebitEnabled")
    cc_emails: List[StrictStr] = Field(alias="ccEmails")
    credit_card_enabled: StrictBool = Field(alias="creditCardEnabled")
    due_date: date = Field(alias="dueDate")
    internal_note: Optional[StrictStr] = Field(default=None, alias="internalNote")
    invoice_date: date = Field(alias="invoiceDate")
    invoice_number: StrictStr = Field(alias="invoiceNumber")
    line_items: List[ApiV1ArLineItemData] = Field(alias="lineItems")
    payer_memo: Optional[StrictStr] = Field(default=None, alias="payerMemo")
    po_number: Optional[StrictStr] = Field(default=None, alias="poNumber")
    service_period_end_date: Optional[date] = Field(default=None, alias="servicePeriodEndDate")
    service_period_start_date: Optional[date] = Field(default=None, alias="servicePeriodStartDate")
    use_real_account_number: StrictBool = Field(alias="useRealAccountNumber")
