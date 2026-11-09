# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Text(ApiModel):
    """Text model."""

    content: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    translated_from_content: Optional[StrictStr] = Field(default=None, alias="translatedFromContent")
    translated_from_language: Optional[StrictStr] = Field(default=None, alias="translatedFromLanguage")
