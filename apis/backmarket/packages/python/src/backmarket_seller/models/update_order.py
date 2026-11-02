# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from backmarket_seller.models.order_line_state import OrderLineState
from backmarket_seller.models.return_reason import ReturnReason
from backmarket_seller.models.vat_type import VatType
from backmarket_seller._runtime import ApiModel


class UpdateOrder(ApiModel):
    """UpdateOrder model."""

    order_id: StrictInt
    new_state: OrderLineState
    sku: Optional[StrictStr] = None
    imei: Optional[Annotated[str, Field(strict=True, max_length=15)]] = None
    serial_number: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    tracking_number: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    tracking_url: Optional[Annotated[str, Field(strict=True, max_length=300)]] = None
    vat_type: Optional[VatType] = None
    date_shipping: Optional[datetime] = None
    shipper: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    return_reason: Optional[ReturnReason] = None
    return_message: Optional[Annotated[str, Field(strict=True, max_length=500)]] = None
