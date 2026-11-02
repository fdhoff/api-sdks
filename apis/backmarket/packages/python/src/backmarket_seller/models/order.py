# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from backmarket_seller.models.address import Address
from backmarket_seller.models.country_code import CountryCode
from backmarket_seller.models.order_line import OrderLine
from backmarket_seller.models.order_state import OrderState
from backmarket_seller._runtime import ApiModel


class Order(ApiModel):
    """Order model."""

    order_id: Optional[StrictInt] = None
    delivery_mode: Optional[StrictStr] = None
    shipping_address: Optional[Address] = None
    billing_address: Optional[Address] = None
    delivery_note: Optional[Annotated[str, Field(strict=True, max_length=300)]] = None
    expected_dispatch_date: Optional[datetime] = None
    tracking_number: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    tracking_url: Optional[Annotated[str, Field(strict=True, max_length=300)]] = None
    shipper_display: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    is_backship: Optional[StrictBool] = None
    date_creation: Optional[datetime] = None
    date_modification: Optional[datetime] = None
    date_shipping: Optional[datetime] = None
    date_payment: Optional[datetime] = None
    state: Optional[OrderState] = None
    orderlines: Optional[List[OrderLine]] = None
    price: Optional[StrictStr] = None
    shipping_price: Optional[StrictStr] = None
    currency: Optional[Annotated[str, Field(strict=True, max_length=3)]] = None
    country_code: Optional[CountryCode] = None
    paypal_reference: Optional[Annotated[str, Field(strict=True, max_length=17)]] = None
    installment_payment: Optional[StrictBool] = None
    payment_method: Optional[StrictStr] = None
    sales_taxes: Optional[StrictStr] = None
