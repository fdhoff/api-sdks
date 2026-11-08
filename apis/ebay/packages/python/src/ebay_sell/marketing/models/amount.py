# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Amount(ApiModel):
    """Amount model."""

    currency: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
