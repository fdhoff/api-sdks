# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CreateSubscriptionFilterRequest(ApiModel):
    """CreateSubscriptionFilterRequest model."""

    filter_schema: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="filterSchema")
