# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.accounts_paginated_response_page import AccountsPaginatedResponsePage
from mercury_banking.models.invest_account import InvestAccount
from mercury_banking._runtime import ApiModel


class InvestAccountsPaginatedResponse(ApiModel):
    """InvestAccountsPaginatedResponse model."""

    accounts: List[InvestAccount]
    page: AccountsPaginatedResponsePage
