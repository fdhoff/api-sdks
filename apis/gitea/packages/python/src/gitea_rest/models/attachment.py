# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class Attachment(ApiModel):
    """Attachment model."""

    browser_download_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    download_count: Optional[StrictInt] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    uuid: Optional[StrictStr] = None
