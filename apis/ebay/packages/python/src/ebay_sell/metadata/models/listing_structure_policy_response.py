# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.listing_structure_policy import ListingStructurePolicy
from ebay_sell._runtime import ApiModel


class ListingStructurePolicyResponse(ApiModel):
    """ListingStructurePolicyResponse model."""

    listing_structure_policies: Optional[List[ListingStructurePolicy]] = Field(
        default=None, alias="listingStructurePolicies"
    )
    warnings: Optional[List[Error]] = None
