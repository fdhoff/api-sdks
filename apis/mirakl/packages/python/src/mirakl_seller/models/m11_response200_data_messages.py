# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.m11_response200_data_messages_attachments import M11Response200DataMessagesAttachments
from mirakl_seller.models.m11_response200_data_messages_from import M11Response200DataMessagesFrom
from mirakl_seller.models.m11_response200_data_messages_to import M11Response200DataMessagesTo
from mirakl_seller._runtime import ApiModel


class M11Response200DataMessages(ApiModel):
    """M11Response200DataMessages model."""

    attachments: Optional[List[M11Response200DataMessagesAttachments]] = None
    body: StrictStr
    date_created: datetime
    var_from: M11Response200DataMessagesFrom = Field(alias="from")
    id: StrictStr
    to: List[M11Response200DataMessagesTo]
