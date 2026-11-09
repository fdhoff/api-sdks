# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.credit_account_statements_paginated_response_page import (
    CreditAccountStatementsPaginatedResponsePage,
)
from mercury_banking.models.depository_account_statement import DepositoryAccountStatement
from mercury_banking._runtime import ApiModel


class DepositoryAccountStatementsPaginatedResponse(ApiModel):
    """DepositoryAccountStatementsPaginatedResponse model."""

    page: CreditAccountStatementsPaginatedResponsePage
    statements: List[DepositoryAccountStatement]
