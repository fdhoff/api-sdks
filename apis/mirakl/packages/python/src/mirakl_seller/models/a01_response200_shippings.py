# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a01_response200_shippings_additional_fields import A01Response200ShippingsAdditionalFields
from mirakl_seller._runtime import ApiModel


class A01Response200Shippings(ApiModel):
    """A01Response200Shippings model."""

    additional_fields: Optional[List[A01Response200ShippingsAdditionalFields]] = None
    shipping_free_amount: Optional[float] = None
    shipping_type_code: StrictStr
    shipping_type_label: StrictStr
    shipping_type_standard_code: Optional[StrictStr] = None
    shipping_zone_code: StrictStr
    shipping_zone_label: StrictStr
