# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.m10_response200_messages_attachments import M10Response200MessagesAttachments
from mirakl_seller.models.m10_response200_messages_from import M10Response200MessagesFrom
from mirakl_seller.models.m10_response200_messages_to import M10Response200MessagesTo
from mirakl_seller._runtime import ApiModel


class M10Response200Messages(ApiModel):
    """M10Response200Messages model."""

    attachments: Optional[List[M10Response200MessagesAttachments]] = None
    body: StrictStr
    date_created: datetime
    var_from: M10Response200MessagesFrom = Field(alias="from")
    id: StrictStr
    to: List[M10Response200MessagesTo]
