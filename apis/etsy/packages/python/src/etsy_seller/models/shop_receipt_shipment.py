# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ShopReceiptShipment(ApiModel):
    """ShopReceiptShipment model."""

    receipt_shipping_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shipment_notification_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    carrier_name: Optional[StrictStr] = None
    tracking_code: Optional[StrictStr] = None
