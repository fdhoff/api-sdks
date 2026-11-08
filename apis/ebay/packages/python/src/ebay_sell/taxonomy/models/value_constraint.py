# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ValueConstraint(ApiModel):
    """ValueConstraint model."""

    applicable_for_localized_aspect_name: Optional[StrictStr] = Field(
        default=None, alias="applicableForLocalizedAspectName"
    )
    applicable_for_localized_aspect_values: Optional[List[StrictStr]] = Field(
        default=None, alias="applicableForLocalizedAspectValues"
    )
