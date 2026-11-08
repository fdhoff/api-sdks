# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.category_aspect import CategoryAspect
from ebay_sell._runtime import ApiModel


class GetCategoriesAspectResponse(ApiModel):
    """GetCategoriesAspectResponse model."""

    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    category_tree_version: Optional[StrictStr] = Field(default=None, alias="categoryTreeVersion")
    category_aspects: Optional[List[CategoryAspect]] = Field(default=None, alias="categoryAspects")
