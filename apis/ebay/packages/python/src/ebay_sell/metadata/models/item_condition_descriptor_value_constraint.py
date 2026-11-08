# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ItemConditionDescriptorValueConstraint(ApiModel):
    """ItemConditionDescriptorValueConstraint model."""

    applicable_to_condition_descriptor_id: Optional[StrictStr] = Field(
        default=None, alias="applicableToConditionDescriptorId"
    )
    applicable_to_condition_descriptor_value_ids: Optional[List[StrictStr]] = Field(
        default=None, alias="applicableToConditionDescriptorValueIds"
    )
