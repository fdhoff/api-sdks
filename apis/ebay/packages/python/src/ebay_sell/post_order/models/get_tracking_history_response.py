# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.scan_detail_type import ScanDetailType
from ebay_sell._runtime import ApiModel


class GetTrackingHistoryResponse(ApiModel):
    """GetTrackingHistoryResponse model."""

    carrier_used: Optional[StrictStr] = Field(default=None, alias="carrierUsed")
    scan_history: Optional[List[ScanDetailType]] = Field(default=None, alias="scanHistory")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
    tracking_status: Optional[StrictStr] = Field(default=None, alias="trackingStatus")
