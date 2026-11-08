# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class LocalListingDistance(ApiModel):
    """LocalListingDistance model."""

    distances: Optional[List[StrictInt]] = None
    distance_type: Optional[StrictStr] = Field(default=None, alias="distanceType")
