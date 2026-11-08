# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.country_policy import CountryPolicy
from ebay_sell._runtime import ApiModel


class RegionalTakeBackPolicies(ApiModel):
    """RegionalTakeBackPolicies model."""

    country_policies: Optional[List[CountryPolicy]] = Field(default=None, alias="countryPolicies")
