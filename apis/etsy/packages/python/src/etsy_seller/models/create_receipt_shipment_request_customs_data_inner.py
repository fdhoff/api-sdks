# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller._runtime import ApiModel


class CreateReceiptShipmentRequestCustomsDataInner(ApiModel):
    """CreateReceiptShipmentRequestCustomsDataInner model."""

    country_of_origin: Optional[StrictStr]
    declared_value: Optional[float]
    hs_code: Optional[StrictStr] = Field(alias="HS_code")
