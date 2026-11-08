# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.developer_analytics.models.resource import Resource
from ebay_sell._runtime import ApiModel


class RateLimit(ApiModel):
    """RateLimit model."""

    api_context: Optional[StrictStr] = Field(default=None, alias="apiContext")
    api_name: Optional[StrictStr] = Field(default=None, alias="apiName")
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion")
    resources: Optional[List[Resource]] = None
