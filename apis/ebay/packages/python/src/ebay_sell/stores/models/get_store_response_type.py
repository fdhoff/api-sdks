# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.stores.models.store_logo_type import StoreLogoType
from ebay_sell._runtime import ApiModel


class GetStoreResponseType(ApiModel):
    """GetStoreResponseType model."""

    description: Optional[StrictStr] = None
    last_opened_time: Optional[StrictStr] = Field(default=None, alias="lastOpenedTime")
    logo: Optional[StoreLogoType] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    url_path: Optional[StrictStr] = Field(default=None, alias="urlPath")
