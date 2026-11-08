# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.return_policy_details import ReturnPolicyDetails
from ebay_sell._runtime import ApiModel


class ReturnPolicy(ApiModel):
    """ReturnPolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    domestic: Optional[ReturnPolicyDetails] = None
    international: Optional[ReturnPolicyDetails] = None
    required: Optional[StrictBool] = None
