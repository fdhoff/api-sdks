# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st12_response200_data import ST12Response200Data
from mirakl_seller._runtime import ApiModel


class ST12Response200(ApiModel):
    """ST12Response200 model."""

    data: List[ST12Response200Data]
    next_page_token: Optional[StrictStr] = None
    previous_page_token: Optional[StrictStr] = None
