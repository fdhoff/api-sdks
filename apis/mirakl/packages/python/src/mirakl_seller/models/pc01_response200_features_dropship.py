# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesDropship(ApiModel):
    """PC01Response200FeaturesDropship model."""

    retail_pricing_edition_enabled: Optional[StrictStr] = None
    retail_pricing_enabled: Optional[StrictBool] = None
