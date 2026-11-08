# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.fulfillment_policy import FulfillmentPolicy
from ebay_sell._runtime import ApiModel


class FulfillmentPolicyResponse(ApiModel):
    """FulfillmentPolicyResponse model."""

    fulfillment_policies: Optional[List[FulfillmentPolicy]] = Field(default=None, alias="fulfillmentPolicies")
    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
