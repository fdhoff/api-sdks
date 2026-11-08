# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.selling_limit import SellingLimit
from ebay_sell._runtime import ApiModel


class SellingPrivileges(ApiModel):
    """SellingPrivileges model."""

    seller_registration_completed: Optional[StrictBool] = Field(default=None, alias="sellerRegistrationCompleted")
    selling_limit: Optional[SellingLimit] = Field(default=None, alias="sellingLimit")
