# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.ad_group import AdGroup
from ebay_sell._runtime import ApiModel


class AdGroupPagedCollectionResponse(ApiModel):
    """AdGroupPagedCollectionResponse model."""

    ad_groups: Optional[List[AdGroup]] = Field(default=None, alias="adGroups")
    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
