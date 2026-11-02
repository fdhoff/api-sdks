# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class BuybackReason(ApiModel):
    """BuybackReason model."""

    message: StrictStr
    identifier: StrictStr
    category: Optional[StrictStr] = None
