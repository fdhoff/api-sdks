# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.developer_analytics.models.rate_limit import RateLimit
from ebay_sell._runtime import ApiModel


class RateLimitsResponse(ApiModel):
    """RateLimitsResponse model."""

    rate_limits: Optional[List[RateLimit]] = Field(default=None, alias="rateLimits")
