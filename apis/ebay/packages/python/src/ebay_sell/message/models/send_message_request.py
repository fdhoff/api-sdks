# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.message.models.message_media import MessageMedia
from ebay_sell.message.models.reference import Reference
from ebay_sell._runtime import ApiModel


class SendMessageRequest(ApiModel):
    """SendMessageRequest model."""

    conversation_id: Optional[StrictStr] = Field(default=None, alias="conversationId")
    email_copy_to_sender: Optional[StrictBool] = Field(default=None, alias="emailCopyToSender")
    message_media: Optional[List[MessageMedia]] = Field(default=None, alias="messageMedia")
    message_text: Optional[StrictStr] = Field(default=None, alias="messageText")
    other_party_username: Optional[StrictStr] = Field(default=None, alias="otherPartyUsername")
    reference: Optional[Reference] = None
