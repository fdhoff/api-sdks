# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.spend_limit import SpendLimit
from mercury_banking._runtime import ApiModel


class UpdateCardRequest(ApiModel):
    """UpdateCardRequest model."""

    nickname: Optional[StrictStr] = None
    spend_limit: Optional[SpendLimit] = Field(default=None, alias="spendLimit")
