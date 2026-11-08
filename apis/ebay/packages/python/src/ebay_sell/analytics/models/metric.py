# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.metric_benchmark import MetricBenchmark
from ebay_sell.analytics.models.metric_distribution import MetricDistribution
from ebay_sell._runtime import ApiModel


class Metric(ApiModel):
    """Metric model."""

    benchmark: Optional[MetricBenchmark] = None
    distributions: Optional[List[MetricDistribution]] = None
    metric_key: Optional[StrictStr] = Field(default=None, alias="metricKey")
    value: Optional[StrictStr] = None
