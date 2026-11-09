# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_report_row_kind import BooksAPIReportRowKind
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking.models.books_ledger_sub_type import BooksLedgerSubType
from mercury_banking.models.books_ledger_type import BooksLedgerType
from mercury_banking._runtime import ApiModel


class BooksAPIReportRow(ApiModel):
    """BooksAPIReportRow model."""

    amounts: List[float]
    children: List[BooksAPIReportRow]
    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    ledger_id: Optional[StrictStr] = Field(default=None, alias="ledgerId")
    name: StrictStr
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    row_kind: BooksAPIReportRowKind = Field(alias="rowKind")
    sort_code: Optional[StrictStr] = Field(default=None, alias="sortCode")
    sub_type: Optional[BooksLedgerSubType] = Field(default=None, alias="subType")
    total_amounts: List[float] = Field(alias="totalAmounts")
    type: Optional[BooksLedgerType] = None


BooksAPIReportRow.model_rebuild(raise_errors=False)
