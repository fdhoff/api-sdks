# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.api_v1_ar_customer_address_input import ApiV1ArCustomerAddressInput
from mercury_banking._runtime import ApiModel


class ApiV1ArCustomerUpdateRequest(ApiModel):
    """ApiV1ArCustomerUpdateRequest model."""

    address: Optional[ApiV1ArCustomerAddressInput] = None
    email: StrictStr
    name: StrictStr
    resend_open_invoices: StrictBool = Field(alias="resendOpenInvoices")
