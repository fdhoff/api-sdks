# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedShipping(ApiModel):
    """A02Response200UpdatedShipping model."""

    lead_time_to_ship: Optional[StrictInt] = None
