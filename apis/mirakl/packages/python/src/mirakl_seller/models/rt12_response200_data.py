# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class RT12Response200Data(ApiModel):
    """RT12Response200Data model."""

    available_return_methods: Optional[List[StrictStr]] = None
    available_return_reasons: Optional[List[StrictStr]] = None
    order_commercial_id: StrictStr
    order_line_id: StrictStr
    return_window: Optional[StrictInt] = None
    return_window_end_date: Optional[datetime] = None
    return_window_start_date: Optional[datetime] = None
    returnable_quantity: StrictInt
