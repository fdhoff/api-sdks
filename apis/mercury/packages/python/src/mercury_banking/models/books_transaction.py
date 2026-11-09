# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_categorizer_type import BooksCategorizerType
from mercury_banking.models.books_transaction_attachment import BooksTransactionAttachment
from mercury_banking.models.books_transaction_posted_status import BooksTransactionPostedStatus
from mercury_banking.models.books_transaction_review_status import BooksTransactionReviewStatus
from mercury_banking.models.mercury_category_with_display import MercuryCategoryWithDisplay
from mercury_banking.models.transaction_method_kind import TransactionMethodKind
from mercury_banking._runtime import ApiModel


class BooksTransaction(ApiModel):
    """BooksTransaction model."""

    amount: float
    attachments: Optional[List[BooksTransactionAttachment]] = None
    card_last_four_digits: Optional[StrictStr] = Field(default=None, alias="cardLastFourDigits")
    categorization_method: Optional[BooksCategorizerType] = Field(default=None, alias="categorizationMethod")
    counterparty_name: Optional[StrictStr] = Field(default=None, alias="counterpartyName")
    custom_category_id: Optional[StrictStr] = Field(default=None, alias="customCategoryId")
    custom_category_name: Optional[StrictStr] = Field(default=None, alias="customCategoryName")
    datetime: StrictStr
    description: StrictStr
    external_metadata_id: Optional[StrictStr] = Field(default=None, alias="externalMetadataId")
    id: StrictStr
    journal_entry_id: Optional[StrictStr] = Field(default=None, alias="journalEntryId")
    ledger_id: Optional[StrictStr] = Field(default=None, alias="ledgerId")
    line_entry_id: Optional[StrictStr] = Field(default=None, alias="lineEntryId")
    merchant_type: Optional[MercuryCategoryWithDisplay] = Field(default=None, alias="merchantType")
    note: Optional[StrictStr] = None
    opposing_line_entry_ids: Optional[List[StrictStr]] = Field(default=None, alias="opposingLineEntryIds")
    personal: StrictBool
    posted_status: BooksTransactionPostedStatus = Field(alias="postedStatus")
    review_status: BooksTransactionReviewStatus = Field(alias="reviewStatus")
    source_account_id: StrictStr = Field(alias="sourceAccountId")
    team_member_id: Optional[StrictStr] = Field(default=None, alias="teamMemberId")
    team_member_name: Optional[StrictStr] = Field(default=None, alias="teamMemberName")
    transaction_method_kind: Optional[TransactionMethodKind] = Field(default=None, alias="transactionMethodKind")
