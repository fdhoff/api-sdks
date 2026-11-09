# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformationPurchaseFeeAmount(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformationPurchaseFeeAmount model."""

    total_amount: float
