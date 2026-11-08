# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.key_management.models.error import Error
from ebay_sell._runtime import ApiModel


class GetSigningKeys429Response(ApiModel):
    """GetSigningKeys429Response model."""

    errors: Optional[List[Error]] = None
