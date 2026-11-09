# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A01Response200Shipping(ApiModel):
    """A01Response200Shipping model."""

    lead_time_to_ship: Optional[StrictInt] = None
