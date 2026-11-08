# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class RateTable(ApiModel):
    """RateTable model."""

    country_code: Optional[StrictStr] = Field(default=None, alias="countryCode")
    locality: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    rate_table_id: Optional[StrictStr] = Field(default=None, alias="rateTableId")
