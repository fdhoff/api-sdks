# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.listing_type_policy import ListingTypePolicy
from ebay_sell._runtime import ApiModel


class ListingTypePoliciesResponse(ApiModel):
    """ListingTypePoliciesResponse model."""

    listing_type_policies: Optional[List[ListingTypePolicy]] = Field(default=None, alias="listingTypePolicies")
    warnings: Optional[List[Error]] = None
