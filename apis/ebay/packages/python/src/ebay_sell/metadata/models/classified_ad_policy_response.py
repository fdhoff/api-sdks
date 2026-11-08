# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.classified_ad_policy import ClassifiedAdPolicy
from ebay_sell.metadata.models.error import Error
from ebay_sell._runtime import ApiModel


class ClassifiedAdPolicyResponse(ApiModel):
    """ClassifiedAdPolicyResponse model."""

    classified_ad_policies: Optional[List[ClassifiedAdPolicy]] = Field(default=None, alias="classifiedAdPolicies")
    warnings: Optional[List[Error]] = None
