# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.item_condition_descriptor import ItemConditionDescriptor
from ebay_sell._runtime import ApiModel


class ItemCondition(ApiModel):
    """ItemCondition model."""

    condition_description: Optional[StrictStr] = Field(default=None, alias="conditionDescription")
    condition_descriptors: Optional[List[ItemConditionDescriptor]] = Field(default=None, alias="conditionDescriptors")
    condition_help_text: Optional[StrictStr] = Field(default=None, alias="conditionHelpText")
    condition_id: Optional[StrictStr] = Field(default=None, alias="conditionId")
    usage: Optional[StrictStr] = None
