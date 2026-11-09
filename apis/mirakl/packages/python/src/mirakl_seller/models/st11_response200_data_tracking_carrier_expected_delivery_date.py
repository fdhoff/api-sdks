# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_tracking_carrier_expected_delivery_date_earliest import (
    ST11Response200DataTrackingCarrierExpectedDeliveryDateEarliest,
)
from mirakl_seller.models.st11_response200_data_tracking_carrier_expected_delivery_date_latest import (
    ST11Response200DataTrackingCarrierExpectedDeliveryDateLatest,
)
from mirakl_seller._runtime import ApiModel


class ST11Response200DataTrackingCarrierExpectedDeliveryDate(ApiModel):
    """ST11Response200DataTrackingCarrierExpectedDeliveryDate model."""

    earliest: Optional[ST11Response200DataTrackingCarrierExpectedDeliveryDateEarliest] = None
    latest: Optional[ST11Response200DataTrackingCarrierExpectedDeliveryDateLatest] = None
