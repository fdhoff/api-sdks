# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class GeneralAttachmentSettings(ApiModel):
    """GeneralAttachmentSettings model."""

    allowed_types: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    max_files: Optional[StrictInt] = None
    max_size: Optional[StrictInt] = None
