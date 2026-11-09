# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.address import Address
from ebay_sell._runtime import ApiModel


class ReturnAddressRequest(ApiModel):
    """ReturnAddressRequest model."""

    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    return_address: Optional[Address] = Field(default=None, alias="returnAddress")
    rma: Optional[StrictStr] = Field(default=None, alias="RMA")
