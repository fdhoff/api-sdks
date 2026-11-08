# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.return_policy import ReturnPolicy
from ebay_sell._runtime import ApiModel


class ReturnPolicyResponse(ApiModel):
    """ReturnPolicyResponse model."""

    return_policies: Optional[List[ReturnPolicy]] = Field(default=None, alias="returnPolicies")
    warnings: Optional[List[Error]] = None
