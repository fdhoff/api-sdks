# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class MarkupOption(ApiModel):
    """MarkupOption model."""

    context: Optional[StrictStr] = Field(default=None, alias="Context")
    file_path: Optional[StrictStr] = Field(default=None, alias="FilePath")
    mode: Optional[StrictStr] = Field(default=None, alias="Mode")
    text: Optional[StrictStr] = Field(default=None, alias="Text")
    wiki: Optional[StrictBool] = Field(default=None, alias="Wiki")
