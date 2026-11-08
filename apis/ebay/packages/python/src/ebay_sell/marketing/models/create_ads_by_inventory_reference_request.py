# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CreateAdsByInventoryReferenceRequest(ApiModel):
    """CreateAdsByInventoryReferenceRequest model."""

    ad_group_id: Optional[StrictStr] = Field(default=None, alias="adGroupId")
    bid_percentage: Optional[StrictStr] = Field(default=None, alias="bidPercentage")
    inventory_reference_id: Optional[StrictStr] = Field(default=None, alias="inventoryReferenceId")
    inventory_reference_type: Optional[StrictStr] = Field(default=None, alias="inventoryReferenceType")
