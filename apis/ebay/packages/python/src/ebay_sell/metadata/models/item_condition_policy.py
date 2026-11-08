# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.item_condition import ItemCondition
from ebay_sell._runtime import ApiModel


class ItemConditionPolicy(ApiModel):
    """ItemConditionPolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    item_condition_required: Optional[StrictBool] = Field(default=None, alias="itemConditionRequired")
    item_conditions: Optional[List[ItemCondition]] = Field(default=None, alias="itemConditions")
