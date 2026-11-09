# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.account_statement import AccountStatement
from mercury_banking.models.credit_account_statements_paginated_response_page import (
    CreditAccountStatementsPaginatedResponsePage,
)
from mercury_banking._runtime import ApiModel


class CreditAccountStatementsPaginatedResponse(ApiModel):
    """CreditAccountStatementsPaginatedResponse model."""

    page: CreditAccountStatementsPaginatedResponsePage
    statements: List[AccountStatement]
