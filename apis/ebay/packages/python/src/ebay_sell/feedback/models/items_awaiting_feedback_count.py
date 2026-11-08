# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ItemsAwaitingFeedbackCount(ApiModel):
    """ItemsAwaitingFeedbackCount model."""

    as_buyer: Optional[StrictInt] = Field(default=None, alias="asBuyer")
    as_seller: Optional[StrictInt] = Field(default=None, alias="asSeller")
