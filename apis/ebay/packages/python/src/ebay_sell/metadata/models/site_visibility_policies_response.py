# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.site_visibility_policy import SiteVisibilityPolicy
from ebay_sell._runtime import ApiModel


class SiteVisibilityPoliciesResponse(ApiModel):
    """SiteVisibilityPoliciesResponse model."""

    site_visibility_policies: Optional[List[SiteVisibilityPolicy]] = Field(default=None, alias="siteVisibilityPolicies")
    warnings: Optional[List[Error]] = None
