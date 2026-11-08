# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.item_condition_policy import ItemConditionPolicy
from ebay_sell._runtime import ApiModel


class ItemConditionPolicyResponse(ApiModel):
    """ItemConditionPolicyResponse model."""

    item_condition_policies: Optional[List[ItemConditionPolicy]] = Field(default=None, alias="itemConditionPolicies")
    warnings: Optional[List[Error]] = None
