# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_report_column import BooksAPIReportColumn
from mercury_banking.models.books_api_report_row import BooksAPIReportRow
from mercury_banking.models.books_api_retained_earnings import BooksAPIRetainedEarnings
from mercury_banking._runtime import ApiModel


class BooksAPIReport(ApiModel):
    """BooksAPIReport model."""

    columns: List[BooksAPIReportColumn]
    retained_earnings: Optional[BooksAPIRetainedEarnings] = Field(default=None, alias="retainedEarnings")
    rows: List[BooksAPIReportRow]
