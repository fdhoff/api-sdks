# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class BulkConversation(ApiModel):
    """BulkConversation model."""

    conversation_id: Optional[StrictStr] = Field(default=None, alias="conversationId")
    conversation_status: Optional[StrictStr] = Field(default=None, alias="conversationStatus")
    conversation_type: Optional[StrictStr] = Field(default=None, alias="conversationType")
