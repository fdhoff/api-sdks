# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.sh12_response200_shipping_types import SH12Response200ShippingTypes
from mirakl_seller._runtime import ApiModel


class SH12Response200(ApiModel):
    """SH12Response200 model."""

    shipping_types: Optional[List[SH12Response200ShippingTypes]] = None
