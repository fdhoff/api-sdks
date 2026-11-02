# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from backmarket_seller._runtime import ApiModel


class CategoryTreeAttributesInner(ApiModel):
    """CategoryTreeAttributesInner model."""

    var_field: StrictStr = Field(alias="field")
    field_name: StrictStr
    type: StrictInt
    allowed_values: StrictStr
    required: StrictBool
