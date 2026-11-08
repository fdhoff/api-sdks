# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.error import Error
from ebay_sell.marketing.models.listing_detail import ListingDetail
from ebay_sell._runtime import ApiModel


class ItemsPagedCollection(ApiModel):
    """ItemsPagedCollection model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    listings: Optional[List[ListingDetail]] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
    warnings: Optional[List[Error]] = None
