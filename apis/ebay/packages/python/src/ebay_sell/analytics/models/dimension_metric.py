# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.dimension import Dimension
from ebay_sell.analytics.models.metric import Metric
from ebay_sell._runtime import ApiModel


class DimensionMetric(ApiModel):
    """DimensionMetric model."""

    dimension: Optional[Dimension] = None
    metrics: Optional[List[Metric]] = None
