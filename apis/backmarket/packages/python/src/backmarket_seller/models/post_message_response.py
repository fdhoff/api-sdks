# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.attachment import Attachment
from backmarket_seller._runtime import ApiModel


class PostMessageResponse(ApiModel):
    """PostMessageResponse model."""

    attachment: Optional[Attachment] = None
    attachments: Optional[List[Attachment]] = None
    date_creation: Optional[datetime] = None
    group: Optional[StrictInt] = None
    id: Optional[StrictInt] = None
    message: Optional[StrictStr] = None
    sender: Optional[StrictInt] = None
