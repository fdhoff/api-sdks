# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class ST41Response200ShippingLabelRateSuccesses(ApiModel):
    """ST41Response200ShippingLabelRateSuccesses model."""

    shipment_id: StrictStr
