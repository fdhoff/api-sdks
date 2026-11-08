# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.item_condition_descriptor_value_constraint import ItemConditionDescriptorValueConstraint
from ebay_sell._runtime import ApiModel


class ItemConditionDescriptorValue(ApiModel):
    """ItemConditionDescriptorValue model."""

    condition_descriptor_value_additional_help_text: Optional[List[StrictStr]] = Field(
        default=None, alias="conditionDescriptorValueAdditionalHelpText"
    )
    condition_descriptor_value_constraints: Optional[List[ItemConditionDescriptorValueConstraint]] = Field(
        default=None, alias="conditionDescriptorValueConstraints"
    )
    condition_descriptor_value_help_text: Optional[StrictStr] = Field(
        default=None, alias="conditionDescriptorValueHelpText"
    )
    condition_descriptor_value_id: Optional[StrictStr] = Field(default=None, alias="conditionDescriptorValueId")
    condition_descriptor_value_name: Optional[StrictStr] = Field(default=None, alias="conditionDescriptorValueName")
