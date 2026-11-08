# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.analytics.models.standards_profile import StandardsProfile
from ebay_sell._runtime import ApiModel


class FindSellerStandardsProfilesResponse(ApiModel):
    """FindSellerStandardsProfilesResponse model."""

    standards_profiles: Optional[List[StandardsProfile]] = Field(default=None, alias="standardsProfiles")
