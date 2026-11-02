# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.light_attachment import LightAttachment
from backmarket_seller._runtime import ApiModel


class Message(ApiModel):
    """Message model."""

    id: Optional[StrictInt] = None
    message: Optional[StrictStr] = None
    date_creation: Optional[datetime] = None
    attachments: Optional[List[LightAttachment]] = None
    initiator: Optional[StrictStr] = None
    kind: Optional[StrictStr] = None
    is_informative: Optional[StrictBool] = None
