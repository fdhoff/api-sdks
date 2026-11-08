# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.message.models.message_detail import MessageDetail
from ebay_sell._runtime import ApiModel


class ConversationDetail(ApiModel):
    """ConversationDetail model."""

    conversation_id: Optional[StrictStr] = Field(default=None, alias="conversationId")
    conversation_status: Optional[StrictStr] = Field(default=None, alias="conversationStatus")
    conversation_title: Optional[StrictStr] = Field(default=None, alias="conversationTitle")
    conversation_type: Optional[StrictStr] = Field(default=None, alias="conversationType")
    created_date: Optional[StrictStr] = Field(default=None, alias="createdDate")
    latest_message: Optional[MessageDetail] = Field(default=None, alias="latestMessage")
    reference_id: Optional[StrictStr] = Field(default=None, alias="referenceId")
    reference_type: Optional[StrictStr] = Field(default=None, alias="referenceType")
    unread_count: Optional[StrictInt] = Field(default=None, alias="unreadCount")
