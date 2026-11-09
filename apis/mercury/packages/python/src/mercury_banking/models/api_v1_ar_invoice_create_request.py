# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.api_send_email_option import ApiSendEmailOption
from mercury_banking.models.api_v1_ar_line_item_data import ApiV1ArLineItemData
from mercury_banking._runtime import ApiModel


class ApiV1ArInvoiceCreateRequest(ApiModel):
    """ApiV1ArInvoiceCreateRequest model."""

    ach_debit_enabled: StrictBool = Field(alias="achDebitEnabled")
    cc_emails: List[StrictStr] = Field(alias="ccEmails")
    credit_card_enabled: StrictBool = Field(alias="creditCardEnabled")
    currency_code: Optional[StrictStr] = Field(default=None, alias="currencyCode")
    customer_id: UUID = Field(alias="customerId")
    destination_account_id: UUID = Field(alias="destinationAccountId")
    due_date: date = Field(alias="dueDate")
    internal_note: Optional[StrictStr] = Field(default=None, alias="internalNote")
    invoice_date: date = Field(alias="invoiceDate")
    invoice_number: Optional[StrictStr] = Field(default=None, alias="invoiceNumber")
    line_items: List[ApiV1ArLineItemData] = Field(alias="lineItems")
    payer_memo: Optional[StrictStr] = Field(default=None, alias="payerMemo")
    po_number: Optional[StrictStr] = Field(default=None, alias="poNumber")
    send_email_option: Optional[ApiSendEmailOption] = Field(default=None, alias="sendEmailOption")
    service_period_end_date: Optional[date] = Field(default=None, alias="servicePeriodEndDate")
    service_period_start_date: Optional[date] = Field(default=None, alias="servicePeriodStartDate")
    use_real_account_number: StrictBool = Field(alias="useRealAccountNumber")
