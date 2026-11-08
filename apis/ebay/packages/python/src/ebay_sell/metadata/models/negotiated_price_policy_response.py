# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.negotiated_price_policy import NegotiatedPricePolicy
from ebay_sell._runtime import ApiModel


class NegotiatedPricePolicyResponse(ApiModel):
    """NegotiatedPricePolicyResponse model."""

    negotiated_price_policies: Optional[List[NegotiatedPricePolicy]] = Field(
        default=None, alias="negotiatedPricePolicies"
    )
    warnings: Optional[List[Error]] = None
