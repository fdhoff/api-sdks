# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PaginationOutput(ApiModel):
    """PaginationOutput model."""

    limit: Optional[StrictInt] = None
    offset: Optional[StrictInt] = None
    total_entries: Optional[StrictInt] = Field(default=None, alias="totalEntries")
    total_pages: Optional[StrictInt] = Field(default=None, alias="totalPages")
