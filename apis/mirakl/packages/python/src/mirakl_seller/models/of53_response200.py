# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of53_response200_error import OF53Response200Error
from mirakl_seller._runtime import ApiModel


class OF53Response200(ApiModel):
    """OF53Response200 model."""

    error: Optional[OF53Response200Error] = None
    last_updated: Optional[datetime] = None
    status: Optional[StrictStr] = None
    urls: Optional[List[StrictStr]] = None
