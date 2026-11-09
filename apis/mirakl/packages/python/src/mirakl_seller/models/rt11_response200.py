# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt11_response200_data import RT11Response200Data
from mirakl_seller._runtime import ApiModel


class RT11Response200(ApiModel):
    """RT11Response200 model."""

    data: List[RT11Response200Data]
    next_page_token: Optional[StrictStr] = None
    previous_page_token: Optional[StrictStr] = None
