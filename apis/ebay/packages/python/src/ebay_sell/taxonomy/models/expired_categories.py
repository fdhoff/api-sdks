# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.expired_category import ExpiredCategory
from ebay_sell._runtime import ApiModel


class ExpiredCategories(ApiModel):
    """ExpiredCategories model."""

    expired_categories: Optional[List[ExpiredCategory]] = Field(default=None, alias="expiredCategories")
