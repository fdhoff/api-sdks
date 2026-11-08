# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.error import Error
from ebay_sell._runtime import ApiModel


class DeleteAdResponse(ApiModel):
    """DeleteAdResponse model."""

    ad_id: Optional[StrictStr] = Field(default=None, alias="adId")
    errors: Optional[List[Error]] = None
    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    status_code: Optional[StrictInt] = Field(default=None, alias="statusCode")
