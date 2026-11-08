# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ItemConditionDescriptorConstraint(ApiModel):
    """ItemConditionDescriptorConstraint model."""

    applicable_to_condition_descriptor_ids: Optional[List[StrictStr]] = Field(
        default=None, alias="applicableToConditionDescriptorIds"
    )
    cardinality: Optional[StrictStr] = None
    default_condition_descriptor_value_id: Optional[StrictStr] = Field(
        default=None, alias="defaultConditionDescriptorValueId"
    )
    max_length: Optional[StrictInt] = Field(default=None, alias="maxLength")
    mode: Optional[StrictStr] = None
    usage: Optional[StrictStr] = None
