# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.ad_reference import AdReference
from ebay_sell.marketing.models.error import Error
from ebay_sell._runtime import ApiModel


class CreateAdsByInventoryReferenceResponse(ApiModel):
    """CreateAdsByInventoryReferenceResponse model."""

    ad_group_id: Optional[StrictStr] = Field(default=None, alias="adGroupId")
    ads: Optional[List[AdReference]] = None
    errors: Optional[List[Error]] = None
    inventory_reference_id: Optional[StrictStr] = Field(default=None, alias="inventoryReferenceId")
    inventory_reference_type: Optional[StrictStr] = Field(default=None, alias="inventoryReferenceType")
    status_code: Optional[StrictInt] = Field(default=None, alias="statusCode")
