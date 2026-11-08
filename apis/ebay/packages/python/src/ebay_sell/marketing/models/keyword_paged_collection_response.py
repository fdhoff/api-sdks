# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.keyword import Keyword
from ebay_sell._runtime import ApiModel


class KeywordPagedCollectionResponse(ApiModel):
    """KeywordPagedCollectionResponse model."""

    href: Optional[StrictStr] = None
    keywords: Optional[List[Keyword]] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
