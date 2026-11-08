# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ExtendedProducerResponsibility(ApiModel):
    """ExtendedProducerResponsibility model."""

    enabled_for_variations: Optional[StrictBool] = Field(default=None, alias="enabledForVariations")
    name: Optional[StrictStr] = None
    usage: Optional[StrictStr] = None
