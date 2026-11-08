# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.notification.models.payload_detail import PayloadDetail
from ebay_sell._runtime import ApiModel


class Topic(ApiModel):
    """Topic model."""

    authorization_scopes: Optional[List[StrictStr]] = Field(default=None, alias="authorizationScopes")
    context: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    filterable: Optional[StrictBool] = None
    scope: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    supported_payloads: Optional[List[PayloadDetail]] = Field(default=None, alias="supportedPayloads")
    topic_id: Optional[StrictStr] = Field(default=None, alias="topicId")
