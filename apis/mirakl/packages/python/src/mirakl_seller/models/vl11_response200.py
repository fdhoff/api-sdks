# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.vl11_response200_values_lists import VL11Response200ValuesLists
from mirakl_seller._runtime import ApiModel


class VL11Response200(ApiModel):
    """VL11Response200 model."""

    values_lists: Optional[List[VL11Response200ValuesLists]] = None
