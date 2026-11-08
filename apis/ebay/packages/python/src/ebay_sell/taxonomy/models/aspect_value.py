# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.value_constraint import ValueConstraint
from ebay_sell._runtime import ApiModel


class AspectValue(ApiModel):
    """AspectValue model."""

    localized_value: Optional[StrictStr] = Field(default=None, alias="localizedValue")
    value_constraints: Optional[List[ValueConstraint]] = Field(default=None, alias="valueConstraints")
