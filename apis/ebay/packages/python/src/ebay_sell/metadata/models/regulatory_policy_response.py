# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.regulatory_policy import RegulatoryPolicy
from ebay_sell._runtime import ApiModel


class RegulatoryPolicyResponse(ApiModel):
    """RegulatoryPolicyResponse model."""

    regulatory_policies: Optional[List[RegulatoryPolicy]] = Field(default=None, alias="regulatoryPolicies")
    warnings: Optional[List[Error]] = None
