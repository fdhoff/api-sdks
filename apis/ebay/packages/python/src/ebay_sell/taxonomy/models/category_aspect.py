# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.aspect import Aspect
from ebay_sell.taxonomy.models.category import Category
from ebay_sell._runtime import ApiModel


class CategoryAspect(ApiModel):
    """CategoryAspect model."""

    category: Optional[Category] = None
    aspects: Optional[List[Aspect]] = None
