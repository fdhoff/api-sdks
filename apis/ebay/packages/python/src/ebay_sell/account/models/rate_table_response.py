# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.rate_table import RateTable
from ebay_sell._runtime import ApiModel


class RateTableResponse(ApiModel):
    """RateTableResponse model."""

    rate_tables: Optional[List[RateTable]] = Field(default=None, alias="rateTables")
