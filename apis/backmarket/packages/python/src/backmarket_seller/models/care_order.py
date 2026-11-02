# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.care_address import CareAddress
from backmarket_seller._runtime import ApiModel


class CareOrder(ApiModel):
    """CareOrder model."""

    order_id: Optional[StrictInt] = None
    shipping_address: Optional[CareAddress] = None
    billing_address: Optional[CareAddress] = None
    tracking_number: Optional[StrictStr] = None
    tracking_url: Optional[StrictStr] = None
    shipper: Optional[StrictInt] = None
    shipper_display: Optional[StrictStr] = None
    date_creation: Optional[datetime] = None
    date_modification: Optional[datetime] = None
    date_shipping: Optional[datetime] = None
    date_payment: Optional[datetime] = None
    state: Optional[StrictInt] = None
    price: Optional[StrictStr] = None
    shipping_price: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = None
