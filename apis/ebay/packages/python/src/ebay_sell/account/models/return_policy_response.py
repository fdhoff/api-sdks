# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.return_policy import ReturnPolicy
from ebay_sell._runtime import ApiModel


class ReturnPolicyResponse(ApiModel):
    """ReturnPolicyResponse model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    return_policies: Optional[List[ReturnPolicy]] = Field(default=None, alias="returnPolicies")
    total: Optional[StrictInt] = None
