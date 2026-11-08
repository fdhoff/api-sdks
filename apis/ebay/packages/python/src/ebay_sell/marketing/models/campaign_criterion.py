# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.selection_rule import SelectionRule
from ebay_sell._runtime import ApiModel


class CampaignCriterion(ApiModel):
    """CampaignCriterion model."""

    auto_select_future_inventory: Optional[StrictBool] = Field(default=None, alias="autoSelectFutureInventory")
    criterion_type: Optional[StrictStr] = Field(default=None, alias="criterionType")
    selection_rules: Optional[List[SelectionRule]] = Field(default=None, alias="selectionRules")
