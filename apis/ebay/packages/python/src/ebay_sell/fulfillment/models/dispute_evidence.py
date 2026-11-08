# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.file_info import FileInfo
from ebay_sell.fulfillment.models.order_line_items import OrderLineItems
from ebay_sell.fulfillment.models.tracking_info import TrackingInfo
from ebay_sell._runtime import ApiModel


class DisputeEvidence(ApiModel):
    """DisputeEvidence model."""

    evidence_id: Optional[StrictStr] = Field(default=None, alias="evidenceId")
    evidence_type: Optional[StrictStr] = Field(default=None, alias="evidenceType")
    files: Optional[List[FileInfo]] = None
    line_items: Optional[List[OrderLineItems]] = Field(default=None, alias="lineItems")
    provided_date: Optional[StrictStr] = Field(default=None, alias="providedDate")
    request_date: Optional[StrictStr] = Field(default=None, alias="requestDate")
    respond_by_date: Optional[StrictStr] = Field(default=None, alias="respondByDate")
    shipment_tracking: Optional[List[TrackingInfo]] = Field(default=None, alias="shipmentTracking")
