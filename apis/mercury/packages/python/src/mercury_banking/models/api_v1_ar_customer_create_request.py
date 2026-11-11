# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.api_v1_ar_customer_address_input import ApiV1ArCustomerAddressInput
from mercury_banking._runtime import ApiModel


class ApiV1ArCustomerCreateRequest(ApiModel):
    """ApiV1ArCustomerCreateRequest model."""

    address: Optional[ApiV1ArCustomerAddressInput] = None
    email: StrictStr
    name: Annotated[str, Field(min_length=1, strict=True, max_length=5000)]
