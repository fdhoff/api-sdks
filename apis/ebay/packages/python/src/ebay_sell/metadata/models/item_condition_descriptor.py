# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.item_condition_descriptor_constraint import ItemConditionDescriptorConstraint
from ebay_sell.metadata.models.item_condition_descriptor_value import ItemConditionDescriptorValue
from ebay_sell._runtime import ApiModel


class ItemConditionDescriptor(ApiModel):
    """ItemConditionDescriptor model."""

    condition_descriptor_constraint: Optional[ItemConditionDescriptorConstraint] = Field(
        default=None, alias="conditionDescriptorConstraint"
    )
    condition_descriptor_help_text: Optional[StrictStr] = Field(default=None, alias="conditionDescriptorHelpText")
    condition_descriptor_id: Optional[StrictStr] = Field(default=None, alias="conditionDescriptorId")
    condition_descriptor_name: Optional[StrictStr] = Field(default=None, alias="conditionDescriptorName")
    condition_descriptor_values: Optional[List[ItemConditionDescriptorValue]] = Field(
        default=None, alias="conditionDescriptorValues"
    )
