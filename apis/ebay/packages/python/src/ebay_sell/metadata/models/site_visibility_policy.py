# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class SiteVisibilityPolicy(ApiModel):
    """SiteVisibilityPolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    cross_border_trade_australia_enabled: Optional[StrictBool] = Field(
        default=None, alias="crossBorderTradeAustraliaEnabled"
    )
    cross_border_trade_gb_enabled: Optional[StrictBool] = Field(default=None, alias="crossBorderTradeGBEnabled")
    cross_border_trade_north_america_enabled: Optional[StrictBool] = Field(
        default=None, alias="crossBorderTradeNorthAmericaEnabled"
    )
