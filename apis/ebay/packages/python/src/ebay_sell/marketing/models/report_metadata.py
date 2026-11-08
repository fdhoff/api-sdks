# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.dimension_metadata import DimensionMetadata
from ebay_sell.marketing.models.metric_metadata import MetricMetadata
from ebay_sell._runtime import ApiModel


class ReportMetadata(ApiModel):
    """ReportMetadata model."""

    dimension_metadata: Optional[List[DimensionMetadata]] = Field(default=None, alias="dimensionMetadata")
    max_number_of_dimensions_to_request: Optional[StrictInt] = Field(
        default=None, alias="maxNumberOfDimensionsToRequest"
    )
    max_number_of_metrics_to_request: Optional[StrictInt] = Field(default=None, alias="maxNumberOfMetricsToRequest")
    channel: Optional[StrictStr] = None
    metric_metadata: Optional[List[MetricMetadata]] = Field(default=None, alias="metricMetadata")
    report_type: Optional[StrictStr] = Field(default=None, alias="reportType")
