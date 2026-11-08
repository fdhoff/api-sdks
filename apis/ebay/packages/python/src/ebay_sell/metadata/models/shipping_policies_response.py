# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.shipping_policy import ShippingPolicy
from ebay_sell._runtime import ApiModel


class ShippingPoliciesResponse(ApiModel):
    """ShippingPoliciesResponse model."""

    shipping_policies: Optional[List[ShippingPolicy]] = Field(default=None, alias="shippingPolicies")
    warnings: Optional[List[Error]] = None
