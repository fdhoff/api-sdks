# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class AspectConstraint(ApiModel):
    """AspectConstraint model."""

    aspect_applicable_to: Optional[List[StrictStr]] = Field(default=None, alias="aspectApplicableTo")
    aspect_data_type: Optional[StrictStr] = Field(default=None, alias="aspectDataType")
    aspect_enabled_for_variations: Optional[StrictBool] = Field(default=None, alias="aspectEnabledForVariations")
    aspect_format: Optional[StrictStr] = Field(default=None, alias="aspectFormat")
    aspect_max_length: Optional[StrictInt] = Field(default=None, alias="aspectMaxLength")
    aspect_mode: Optional[StrictStr] = Field(default=None, alias="aspectMode")
    aspect_required: Optional[StrictBool] = Field(default=None, alias="aspectRequired")
    aspect_usage: Optional[StrictStr] = Field(default=None, alias="aspectUsage")
    expected_required_by_date: Optional[StrictStr] = Field(default=None, alias="expectedRequiredByDate")
    item_to_aspect_cardinality: Optional[StrictStr] = Field(default=None, alias="itemToAspectCardinality")
    aspect_advanced_data_type: Optional[StrictStr] = Field(default=None, alias="aspectAdvancedDataType")
