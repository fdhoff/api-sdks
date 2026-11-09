# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.account_statement_transaction import AccountStatementTransaction
from mercury_banking.models.address import Address
from mercury_banking._runtime import ApiModel


class DepositoryAccountStatement(ApiModel):
    """DepositoryAccountStatement model."""

    account_number: StrictStr = Field(alias="accountNumber")
    company_legal_address: Address = Field(alias="companyLegalAddress")
    company_legal_name: StrictStr = Field(alias="companyLegalName")
    download_url: StrictStr = Field(alias="downloadUrl")
    ein: Optional[StrictStr] = None
    end_date: StrictStr = Field(alias="endDate")
    ending_balance: float = Field(alias="endingBalance")
    id: UUID
    routing_number: StrictStr = Field(alias="routingNumber")
    start_date: StrictStr = Field(alias="startDate")
    transactions: List[AccountStatementTransaction]
