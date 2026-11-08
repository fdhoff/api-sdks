# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.message.models.conversations_metadata import ConversationsMetadata
from ebay_sell.message.models.conversations_response import ConversationsResponse
from ebay_sell._runtime import ApiModel


class BulkUpdateConversationsResponse(ApiModel):
    """BulkUpdateConversationsResponse model."""

    conversations_metadata: Optional[ConversationsMetadata] = Field(default=None, alias="conversationsMetadata")
    conversations_response: Optional[List[ConversationsResponse]] = Field(default=None, alias="conversationsResponse")
