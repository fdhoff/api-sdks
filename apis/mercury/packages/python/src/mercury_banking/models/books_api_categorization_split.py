# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class BooksAPICategorizationSplit(ApiModel):
    """BooksAPICategorizationSplit model."""

    amount: float
    description: Optional[StrictStr] = None
    ledger_id: StrictStr = Field(alias="ledgerId")
    tag_ids: Optional[List[StrictStr]] = Field(default=None, alias="tagIds")
