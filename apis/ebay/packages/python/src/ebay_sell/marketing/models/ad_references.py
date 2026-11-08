# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.ad_reference import AdReference
from ebay_sell._runtime import ApiModel


class AdReferences(ApiModel):
    """AdReferences model."""

    ads: Optional[List[AdReference]] = None
