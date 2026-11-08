# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.message.models.message_media import MessageMedia
from ebay_sell._runtime import ApiModel


class SendMessageResponse(ApiModel):
    """SendMessageResponse model."""

    created_date: Optional[StrictStr] = Field(default=None, alias="createdDate")
    message_body: Optional[StrictStr] = Field(default=None, alias="messageBody")
    message_id: Optional[StrictStr] = Field(default=None, alias="messageId")
    message_media: Optional[List[MessageMedia]] = Field(default=None, alias="messageMedia")
    read_status: Optional[StrictBool] = Field(default=None, alias="readStatus")
    recipient_user_name: Optional[StrictStr] = Field(default=None, alias="recipientUserName")
    sender_user_name: Optional[StrictStr] = Field(default=None, alias="senderUserName")
    subject: Optional[StrictStr] = None
