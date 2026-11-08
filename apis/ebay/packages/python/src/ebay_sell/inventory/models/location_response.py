# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.inventory_location_response import InventoryLocationResponse
from ebay_sell._runtime import ApiModel


class LocationResponse(ApiModel):
    """LocationResponse model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
    locations: Optional[List[InventoryLocationResponse]] = None
