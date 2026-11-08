# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.message.models.message_detail import MessageDetail
from ebay_sell._runtime import ApiModel


class GetMessagesByConversationIdResponse(ApiModel):
    """GetMessagesByConversationIdResponse model."""

    conversation_status: Optional[StrictStr] = Field(default=None, alias="conversationStatus")
    conversation_title: Optional[StrictStr] = Field(default=None, alias="conversationTitle")
    conversation_type: Optional[StrictStr] = Field(default=None, alias="conversationType")
    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    messages: Optional[List[MessageDetail]] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
