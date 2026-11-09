# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.address import Address
from ebay_sell._runtime import ApiModel


class ReturnAddress(ApiModel):
    """ReturnAddress model."""

    address: Optional[Address] = None
    editable: Optional[StrictBool] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    rma: Optional[StrictStr] = Field(default=None, alias="RMA")
