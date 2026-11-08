# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CustomerServiceMetricsFilterCriteria(ApiModel):
    """CustomerServiceMetricsFilterCriteria model."""

    customer_service_metric_type: Optional[StrictStr] = Field(default=None, alias="customerServiceMetricType")
    evaluation_marketplace_id: Optional[StrictStr] = Field(default=None, alias="evaluationMarketplaceId")
    listing_categories: Optional[List[StrictStr]] = Field(default=None, alias="listingCategories")
    shipping_regions: Optional[List[StrictStr]] = Field(default=None, alias="shippingRegions")
