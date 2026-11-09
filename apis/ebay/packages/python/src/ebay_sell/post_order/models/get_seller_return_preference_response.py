# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class GetSellerReturnPreferenceResponse(ApiModel):
    """GetSellerReturnPreferenceResponse model."""

    advance_rules_enabled: Optional[StrictBool] = Field(default=None, alias="advanceRulesEnabled")
    rma_required: Optional[StrictBool] = Field(default=None, alias="rmaRequired")
    version_id: Optional[StrictInt] = Field(default=None, alias="versionId")
