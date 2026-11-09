# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_cash_balance_row import BooksAPICashBalanceRow
from mercury_banking.models.books_api_cash_flow_ledger_row import BooksAPICashFlowLedgerRow
from mercury_banking.models.books_api_report_column import BooksAPIReportColumn
from mercury_banking._runtime import ApiModel


class BooksAPICashFlowReport(ApiModel):
    """BooksAPICashFlowReport model."""

    columns: List[BooksAPIReportColumn]
    ending_balances: List[BooksAPICashBalanceRow] = Field(alias="endingBalances")
    ending_cash_balances: List[float] = Field(alias="endingCashBalances")
    ledgers: List[BooksAPICashFlowLedgerRow]
    starting_balances: List[BooksAPICashBalanceRow] = Field(alias="startingBalances")
    starting_cash_balances: List[float] = Field(alias="startingCashBalances")
