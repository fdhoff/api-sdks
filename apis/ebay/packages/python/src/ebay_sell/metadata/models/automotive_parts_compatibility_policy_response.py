# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.automotive_parts_compatibility_policy import AutomotivePartsCompatibilityPolicy
from ebay_sell.metadata.models.error import Error
from ebay_sell._runtime import ApiModel


class AutomotivePartsCompatibilityPolicyResponse(ApiModel):
    """AutomotivePartsCompatibilityPolicyResponse model."""

    automotive_parts_compatibility_policies: Optional[List[AutomotivePartsCompatibilityPolicy]] = Field(
        default=None, alias="automotivePartsCompatibilityPolicies"
    )
    warnings: Optional[List[Error]] = None
