# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class EndOfAuctionEmailPreferencesType(ApiModel):
    """EndOfAuctionEmailPreferencesType model."""

    email_customized: Optional[StrictBool] = Field(default=None, alias="emailCustomized")
    logo_customized: Optional[StrictBool] = Field(default=None, alias="logoCustomized")
    logo_type: Optional[StrictStr] = Field(default=None, alias="logoType")
    logo_url: Optional[StrictStr] = Field(default=None, alias="logoUrl")
    template_text: Optional[StrictStr] = Field(default=None, alias="templateText")
    text_customized: Optional[StrictBool] = Field(default=None, alias="textCustomized")
