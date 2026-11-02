# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class Attachment(ApiModel):
    """Attachment model."""

    msg: Optional[StrictInt] = None
    group: Optional[StrictInt] = None
    sender: Optional[StrictInt] = None
    attachment: Optional[StrictStr] = None
