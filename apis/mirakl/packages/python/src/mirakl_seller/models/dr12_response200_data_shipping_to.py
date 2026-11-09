# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr12_response200_data_shipping_to_address import DR12Response200DataShippingToAddress
from mirakl_seller._runtime import ApiModel


class DR12Response200DataShippingTo(ApiModel):
    """DR12Response200DataShippingTo model."""

    address: Optional[DR12Response200DataShippingToAddress] = None
