# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class RT01Response200ReturnErrors(ApiModel):
    """RT01Response200ReturnErrors model."""

    message: Optional[StrictStr] = None
    order_commercial_id: Optional[StrictStr] = None
