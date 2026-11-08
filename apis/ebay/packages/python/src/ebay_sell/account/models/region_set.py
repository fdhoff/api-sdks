# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.region import Region
from ebay_sell._runtime import ApiModel


class RegionSet(ApiModel):
    """RegionSet model."""

    region_excluded: Optional[List[Region]] = Field(default=None, alias="regionExcluded")
    region_included: Optional[List[Region]] = Field(default=None, alias="regionIncluded")
