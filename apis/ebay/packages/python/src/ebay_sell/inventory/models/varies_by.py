# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.specification import Specification
from ebay_sell._runtime import ApiModel


class VariesBy(ApiModel):
    """VariesBy model."""

    aspects_image_varies_by: Optional[List[StrictStr]] = Field(default=None, alias="aspectsImageVariesBy")
    specifications: Optional[List[Specification]] = None
