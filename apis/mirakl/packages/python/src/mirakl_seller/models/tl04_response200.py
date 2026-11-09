# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl04_response200_error import TL04Response200Error
from mirakl_seller._runtime import ApiModel


class TL04Response200(ApiModel):
    """TL04Response200 model."""

    error: Optional[TL04Response200Error] = None
    last_updated: Optional[datetime] = None
    status: Optional[StrictStr] = None
    urls: Optional[List[StrictStr]] = None
