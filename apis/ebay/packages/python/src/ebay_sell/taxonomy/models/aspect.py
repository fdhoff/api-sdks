# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.aspect_constraint import AspectConstraint
from ebay_sell.taxonomy.models.aspect_value import AspectValue
from ebay_sell.taxonomy.models.relevance_indicator import RelevanceIndicator
from ebay_sell._runtime import ApiModel


class Aspect(ApiModel):
    """Aspect model."""

    aspect_constraint: Optional[AspectConstraint] = Field(default=None, alias="aspectConstraint")
    aspect_values: Optional[List[AspectValue]] = Field(default=None, alias="aspectValues")
    localized_aspect_name: Optional[StrictStr] = Field(default=None, alias="localizedAspectName")
    relevance_indicator: Optional[RelevanceIndicator] = Field(default=None, alias="relevanceIndicator")
