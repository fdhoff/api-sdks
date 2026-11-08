# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.category_policy import CategoryPolicy
from ebay_sell.metadata.models.error import Error
from ebay_sell._runtime import ApiModel


class CategoryPolicyResponse(ApiModel):
    """CategoryPolicyResponse model."""

    category_policies: Optional[List[CategoryPolicy]] = Field(default=None, alias="categoryPolicies")
    warnings: Optional[List[Error]] = None
