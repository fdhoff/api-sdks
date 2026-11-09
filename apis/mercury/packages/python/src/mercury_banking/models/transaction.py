# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.category_data import CategoryData
from mercury_banking.models.currency_exchange_info import CurrencyExchangeInfo
from mercury_banking.models.gl_allocation import GlAllocation
from mercury_banking.models.merchant_data import MerchantData
from mercury_banking.models.mercury_category import MercuryCategory
from mercury_banking.models.related_transaction_data import RelatedTransactionData
from mercury_banking.models.transaction_accounting_status import TransactionAccountingStatus
from mercury_banking.models.transaction_attachment import TransactionAttachment
from mercury_banking.models.transaction_kind import TransactionKind
from mercury_banking.models.transaction_method_data import TransactionMethodData
from mercury_banking.models.transaction_status import TransactionStatus
from mercury_banking._runtime import ApiModel


class Transaction(ApiModel):
    """Transaction model."""

    account_id: UUID = Field(alias="accountId")
    accounting_status: Optional[TransactionAccountingStatus] = Field(default=None, alias="accountingStatus")
    amount: Annotated[float, Field(multiple_of=0.01)]
    attachments: List[TransactionAttachment]
    bank_description: Optional[StrictStr] = Field(default=None, alias="bankDescription")
    card_id: Optional[UUID] = Field(default=None, alias="cardId")
    category_data: Optional[CategoryData] = Field(default=None, alias="categoryData")
    check_number: Optional[StrictStr] = Field(default=None, alias="checkNumber")
    compliant_with_receipt_policy: StrictBool = Field(alias="compliantWithReceiptPolicy")
    counterparty_id: UUID = Field(alias="counterpartyId")
    counterparty_name: StrictStr = Field(alias="counterpartyName")
    counterparty_nickname: Optional[StrictStr] = Field(default=None, alias="counterpartyNickname")
    created_at: StrictStr = Field(alias="createdAt")
    credit_account_period_id: Optional[UUID] = Field(default=None, alias="creditAccountPeriodId")
    currency_exchange_info: Optional[CurrencyExchangeInfo] = Field(default=None, alias="currencyExchangeInfo")
    dashboard_link: StrictStr = Field(alias="dashboardLink")
    details: Optional[TransactionMethodData] = None
    estimated_delivery_date: StrictStr = Field(alias="estimatedDeliveryDate")
    external_memo: Optional[StrictStr] = Field(default=None, alias="externalMemo")
    failed_at: Optional[StrictStr] = Field(default=None, alias="failedAt")
    fee_id: Optional[UUID] = Field(default=None, alias="feeId")
    general_ledger_code_name: Optional[StrictStr] = Field(default=None, alias="generalLedgerCodeName")
    gl_allocations: List[GlAllocation] = Field(alias="glAllocations")
    has_generated_receipt: StrictBool = Field(alias="hasGeneratedReceipt")
    id: UUID
    kind: TransactionKind
    merchant: Optional[MerchantData] = None
    mercury_category: Optional[MercuryCategory] = Field(default=None, alias="mercuryCategory")
    note: Optional[StrictStr] = None
    posted_at: Optional[StrictStr] = Field(default=None, alias="postedAt")
    reason_for_failure: Optional[StrictStr] = Field(default=None, alias="reasonForFailure")
    related_transactions: List[RelatedTransactionData] = Field(alias="relatedTransactions")
    request_id: Optional[StrictStr] = Field(default=None, alias="requestId")
    status: TransactionStatus
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
