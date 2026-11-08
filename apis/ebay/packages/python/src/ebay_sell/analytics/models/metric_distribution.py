# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.distribution import Distribution
from ebay_sell._runtime import ApiModel


class MetricDistribution(ApiModel):
    """MetricDistribution model."""

    basis: Optional[StrictStr] = None
    data: Optional[List[Distribution]] = None
