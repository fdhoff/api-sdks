# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st51_response200_shipping_label_errors import ST51Response200ShippingLabelErrors
from mirakl_seller.models.st51_response200_shipping_label_successes import ST51Response200ShippingLabelSuccesses
from mirakl_seller._runtime import ApiModel


class ST51Response200(ApiModel):
    """ST51Response200 model."""

    shipping_label_errors: List[ST51Response200ShippingLabelErrors]
    shipping_label_successes: List[ST51Response200ShippingLabelSuccesses]
