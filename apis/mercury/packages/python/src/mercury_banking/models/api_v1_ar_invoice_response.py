# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.api_v1_ar_line_item_data import ApiV1ArLineItemData
from mercury_banking.models.payment_link_status import PaymentLinkStatus
from mercury_banking._runtime import ApiModel


class ApiV1ArInvoiceResponse(ApiModel):
    """ApiV1ArInvoiceResponse model."""

    ach_debit_enabled: StrictBool = Field(alias="achDebitEnabled")
    amount: Annotated[float, Field(multiple_of=0.01)]
    canceled_at: Optional[StrictStr] = Field(default=None, alias="canceledAt")
    cc_emails: List[StrictStr] = Field(alias="ccEmails")
    created_at: StrictStr = Field(alias="createdAt")
    credit_card_enabled: StrictBool = Field(alias="creditCardEnabled")
    currency_code: StrictStr = Field(alias="currencyCode")
    customer_id: UUID = Field(alias="customerId")
    destination_account_id: UUID = Field(alias="destinationAccountId")
    due_date: date = Field(alias="dueDate")
    id: UUID
    internal_note: Optional[StrictStr] = Field(default=None, alias="internalNote")
    invoice_date: date = Field(alias="invoiceDate")
    invoice_number: StrictStr = Field(alias="invoiceNumber")
    line_items: List[ApiV1ArLineItemData] = Field(alias="lineItems")
    payer_memo: Optional[StrictStr] = Field(default=None, alias="payerMemo")
    po_number: Optional[StrictStr] = Field(default=None, alias="poNumber")
    service_period_end_date: Optional[date] = Field(default=None, alias="servicePeriodEndDate")
    service_period_start_date: Optional[date] = Field(default=None, alias="servicePeriodStartDate")
    slug: StrictStr
    status: PaymentLinkStatus
    updated_at: StrictStr = Field(alias="updatedAt")
    use_real_account_number: StrictBool = Field(alias="useRealAccountNumber")
