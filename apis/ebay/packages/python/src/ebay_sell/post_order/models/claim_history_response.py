# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.claim_history_event_model import ClaimHistoryEventModel
from ebay_sell.post_order.models.shipment_tracking_detail_type import ShipmentTrackingDetailType
from ebay_sell._runtime import ApiModel


class ClaimHistoryResponse(ApiModel):
    """ClaimHistoryResponse model."""

    history: Optional[List[ClaimHistoryEventModel]] = None
    shipment_tracking_details: Optional[ShipmentTrackingDetailType] = Field(
        default=None, alias="shipmentTrackingDetails"
    )
