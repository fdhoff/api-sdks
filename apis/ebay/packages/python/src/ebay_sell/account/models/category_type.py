# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CategoryType(ApiModel):
    """CategoryType model."""

    default: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
