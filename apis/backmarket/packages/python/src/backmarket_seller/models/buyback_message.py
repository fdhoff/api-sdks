# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.buyback_message_author import BuybackMessageAuthor
from backmarket_seller._runtime import ApiModel


class BuybackMessage(ApiModel):
    """BuybackMessage model."""

    body: Optional[StrictStr] = None
    var_date: StrictStr = Field(alias="date")
    attachments: Optional[List[StrictStr]] = None
    author: BuybackMessageAuthor
