# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class RT52Response200DataFilesQrCode(ApiModel):
    """RT52Response200DataFilesQrCode model."""

    file_type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
