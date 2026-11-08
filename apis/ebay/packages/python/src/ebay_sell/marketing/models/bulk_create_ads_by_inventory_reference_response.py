# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.create_ads_by_inventory_reference_response import CreateAdsByInventoryReferenceResponse
from ebay_sell._runtime import ApiModel


class BulkCreateAdsByInventoryReferenceResponse(ApiModel):
    """BulkCreateAdsByInventoryReferenceResponse model."""

    responses: Optional[List[CreateAdsByInventoryReferenceResponse]] = None
