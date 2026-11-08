# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ConversationsMetadata(ApiModel):
    """ConversationsMetadata model."""

    total_conversations_count: Optional[StrictInt] = Field(default=None, alias="totalConversationsCount")
    update_failure_count: Optional[StrictInt] = Field(default=None, alias="updateFailureCount")
    update_success_count: Optional[StrictInt] = Field(default=None, alias="updateSuccessCount")
