# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class CareFolder(ApiModel):
    """CareFolder model."""

    id: Optional[StrictInt] = None
    client: Optional[StrictInt] = None
    merchant: Optional[StrictInt] = None
    orderline: Optional[StrictInt] = None
    date_creation: Optional[datetime] = None
    date_modification: Optional[datetime] = None
    date_last_message: Optional[datetime] = None
    date_closed: Optional[datetime] = None
    state: Optional[StrictInt] = None
    lines: Optional[List[StrictInt]] = None
    country_code: Optional[StrictStr] = None
    backcare: Optional[StrictBool] = None
