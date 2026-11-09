# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking._runtime import ApiModel


class InternalTransferAPIRequest(ApiModel):
    """InternalTransferAPIRequest model."""

    amount: Annotated[float, Field(ge=0.01)]
    destination_account_id: UUID = Field(alias="destinationAccountId")
    idempotency_key: StrictStr = Field(alias="idempotencyKey")
    note: Optional[StrictStr] = None
    source_account_id: UUID = Field(alias="sourceAccountId")
