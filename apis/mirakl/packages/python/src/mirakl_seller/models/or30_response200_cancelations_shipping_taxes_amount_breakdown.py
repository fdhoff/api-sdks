# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or30_response200_cancelations_shipping_taxes_amount_breakdown_parts import (
    OR30Response200CancelationsShippingTaxesAmountBreakdownParts,
)
from mirakl_seller._runtime import ApiModel


class OR30Response200CancelationsShippingTaxesAmountBreakdown(ApiModel):
    """OR30Response200CancelationsShippingTaxesAmountBreakdown model."""

    parts: Annotated[
        List[OR30Response200CancelationsShippingTaxesAmountBreakdownParts], Field(min_length=1, max_length=2147483647)
    ]
