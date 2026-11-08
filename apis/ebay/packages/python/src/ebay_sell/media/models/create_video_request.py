# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CreateVideoRequest(ApiModel):
    """CreateVideoRequest model."""

    classification: Optional[List[StrictStr]] = None
    description: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
