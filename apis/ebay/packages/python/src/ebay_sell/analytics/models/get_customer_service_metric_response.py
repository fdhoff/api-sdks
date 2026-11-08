# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.dimension_metric import DimensionMetric
from ebay_sell.analytics.models.evaluation_cycle import EvaluationCycle
from ebay_sell._runtime import ApiModel


class GetCustomerServiceMetricResponse(ApiModel):
    """GetCustomerServiceMetricResponse model."""

    dimension_metrics: Optional[List[DimensionMetric]] = Field(default=None, alias="dimensionMetrics")
    evaluation_cycle: Optional[EvaluationCycle] = Field(default=None, alias="evaluationCycle")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
