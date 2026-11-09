# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesPurchaseTax(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesPurchaseTax model."""

    purchase_amount: float
    purchase_rate: Optional[float] = None
