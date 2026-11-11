# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.api_v1_receipt_status import ApiV1ReceiptStatus
from mercury_banking._runtime import ApiModel


class ApiV1ReceiptResponse(ApiModel):
    """ApiV1ReceiptResponse model."""

    created_at: StrictStr = Field(alias="createdAt")
    file_name: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="fileName")
    id: UUID
    matched_transaction_id: Optional[UUID] = Field(default=None, alias="matchedTransactionId")
    status: ApiV1ReceiptStatus
    uploaded_at: Optional[StrictStr] = Field(default=None, alias="uploadedAt")
