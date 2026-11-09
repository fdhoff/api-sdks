# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.account_statement_payload_account_details import AccountStatementPayloadAccountDetails
from mercury_banking._runtime import ApiModel


class AccountStatementPayload(ApiModel):
    """AccountStatementPayload model."""

    account_details: AccountStatementPayloadAccountDetails = Field(alias="accountDetails")
    account_type: StrictStr = Field(alias="accountType")
