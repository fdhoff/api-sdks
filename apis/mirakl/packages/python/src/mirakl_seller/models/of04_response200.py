# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of04_response200_data import OF04Response200Data
from mirakl_seller._runtime import ApiModel


class OF04Response200(ApiModel):
    """OF04Response200 model."""

    data: List[OF04Response200Data]
    next_page_token: Optional[StrictStr] = None
    previous_page_token: Optional[StrictStr] = None
