# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.swift_bank_account_type import SwiftBankAccountType
from mercury_banking._runtime import ApiModel


class InternationalWireDominicanRepublicSpecificData(ApiModel):
    """InternationalWireDominicanRepublicSpecificData model."""

    account_type: SwiftBankAccountType = Field(alias="accountType")
    legal_id: StrictStr = Field(alias="legalId")
