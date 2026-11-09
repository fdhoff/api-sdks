# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_request_type import ReturnRequestType
from ebay_sell._runtime import ApiModel


class CreateReturnRequest(ApiModel):
    """CreateReturnRequest model."""

    draft_id: Optional[StrictStr] = Field(default=None, alias="draftId")
    return_request: Optional[ReturnRequestType] = Field(default=None, alias="returnRequest")
