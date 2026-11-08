# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.delete_ads_by_inventory_reference_response import DeleteAdsByInventoryReferenceResponse
from ebay_sell._runtime import ApiModel


class BulkDeleteAdsByInventoryReferenceResponse(ApiModel):
    """BulkDeleteAdsByInventoryReferenceResponse model."""

    responses: Optional[List[DeleteAdsByInventoryReferenceResponse]] = None
