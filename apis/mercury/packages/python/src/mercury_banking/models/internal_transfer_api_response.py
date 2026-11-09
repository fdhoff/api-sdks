# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.transaction import Transaction
from mercury_banking._runtime import ApiModel


class InternalTransferAPIResponse(ApiModel):
    """InternalTransferAPIResponse model."""

    credit_transaction: Transaction = Field(alias="creditTransaction")
    debit_transaction: Transaction = Field(alias="debitTransaction")
