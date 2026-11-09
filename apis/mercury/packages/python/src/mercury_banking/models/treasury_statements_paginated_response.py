# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.credit_account_statements_paginated_response_page import (
    CreditAccountStatementsPaginatedResponsePage,
)
from mercury_banking.models.treasury_statement import TreasuryStatement
from mercury_banking._runtime import ApiModel


class TreasuryStatementsPaginatedResponse(ApiModel):
    """TreasuryStatementsPaginatedResponse model."""

    page: CreditAccountStatementsPaginatedResponsePage
    statements: List[TreasuryStatement]
