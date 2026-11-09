# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or28_response200_refunds_taxes_amount_breakdown_parts import (
    OR28Response200RefundsTaxesAmountBreakdownParts,
)
from mirakl_seller._runtime import ApiModel


class OR28Response200RefundsTaxesAmountBreakdown(ApiModel):
    """OR28Response200RefundsTaxesAmountBreakdown model."""

    parts: Annotated[List[OR28Response200RefundsTaxesAmountBreakdownParts], Field(min_length=1, max_length=2147483647)]
