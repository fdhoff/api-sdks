# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.backbox import Backbox
from backmarket_seller._runtime import ApiModel


class BackboxPage(ApiModel):
    """BackboxPage model."""

    count: StrictInt
    next: Optional[StrictStr]
    previous: Optional[StrictStr]
    results: List[Backbox]
