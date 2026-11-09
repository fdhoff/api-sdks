# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st41_response200_shipping_label_rate_errors import ST41Response200ShippingLabelRateErrors
from mirakl_seller.models.st41_response200_shipping_label_rate_successes import (
    ST41Response200ShippingLabelRateSuccesses,
)
from mirakl_seller._runtime import ApiModel


class ST41Response200(ApiModel):
    """ST41Response200 model."""

    shipping_label_rate_errors: List[ST41Response200ShippingLabelRateErrors]
    shipping_label_rate_successes: List[ST41Response200ShippingLabelRateSuccesses]
