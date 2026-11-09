# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking._runtime import ApiModel


class ApiV1AssignTransactionRequest(ApiModel):
    """ApiV1AssignTransactionRequest model."""

    allow_overspend: Optional[StrictBool] = Field(default=None, alias="allowOverspend")
    transaction_id: UUID = Field(alias="transactionId")
