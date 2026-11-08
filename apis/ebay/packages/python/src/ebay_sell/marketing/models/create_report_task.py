# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.dimension import Dimension
from ebay_sell.marketing.models.inventory_reference import InventoryReference
from ebay_sell._runtime import ApiModel


class CreateReportTask(ApiModel):
    """CreateReportTask model."""

    additional_records: Optional[List[StrictStr]] = Field(default=None, alias="additionalRecords")
    campaign_ids: Optional[List[StrictStr]] = Field(default=None, alias="campaignIds")
    channels: Optional[List[StrictStr]] = None
    date_from: Optional[StrictStr] = Field(default=None, alias="dateFrom")
    date_to: Optional[StrictStr] = Field(default=None, alias="dateTo")
    dimensions: Optional[List[Dimension]] = None
    funding_models: Optional[List[StrictStr]] = Field(default=None, alias="fundingModels")
    inventory_references: Optional[List[InventoryReference]] = Field(default=None, alias="inventoryReferences")
    listing_ids: Optional[List[StrictStr]] = Field(default=None, alias="listingIds")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    metric_keys: Optional[List[StrictStr]] = Field(default=None, alias="metricKeys")
    report_format: Optional[StrictStr] = Field(default=None, alias="reportFormat")
    report_type: Optional[StrictStr] = Field(default=None, alias="reportType")
