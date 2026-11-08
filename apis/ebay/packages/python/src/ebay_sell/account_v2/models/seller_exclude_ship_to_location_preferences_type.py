# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class SellerExcludeShipToLocationPreferencesType(ApiModel):
    """SellerExcludeShipToLocationPreferencesType model."""

    exclude_ship_to_locations: Optional[List[StrictStr]] = Field(default=None, alias="excludeShipToLocations")
