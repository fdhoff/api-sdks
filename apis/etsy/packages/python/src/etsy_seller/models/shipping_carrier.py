# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.shipping_carrier_mail_class import ShippingCarrierMailClass
from etsy_seller._runtime import ApiModel


class ShippingCarrier(ApiModel):
    """ShippingCarrier model."""

    shipping_carrier_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    name: Optional[StrictStr] = None
    domestic_classes: Optional[List[ShippingCarrierMailClass]] = None
    international_classes: Optional[List[ShippingCarrierMailClass]] = None
