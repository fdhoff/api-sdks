# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.api_v1_ar_customer_address import ApiV1ArCustomerAddress
from mercury_banking._runtime import ApiModel


class ApiV1ArCustomerResponseData(ApiModel):
    """ApiV1ArCustomerResponseData model."""

    address: Optional[ApiV1ArCustomerAddress] = None
    deleted_at: Optional[StrictStr] = Field(default=None, alias="deletedAt")
    email: StrictStr
    id: UUID
    name: StrictStr
