# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.motors_listing_policy import MotorsListingPolicy
from ebay_sell._runtime import ApiModel


class MotorsListingPoliciesResponse(ApiModel):
    """MotorsListingPoliciesResponse model."""

    motors_listing_policies: Optional[List[MotorsListingPolicy]] = Field(default=None, alias="motorsListingPolicies")
    warnings: Optional[List[Error]] = None
