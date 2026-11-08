# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.identity.models.error import Error
from ebay_sell._runtime import ApiModel


class GetUser429Response(ApiModel):
    """GetUser429Response model."""

    errors: Optional[List[Error]] = None
