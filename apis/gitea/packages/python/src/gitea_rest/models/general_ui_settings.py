# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class GeneralUISettings(ApiModel):
    """GeneralUISettings model."""

    allowed_reactions: Optional[List[StrictStr]] = None
    custom_emojis: Optional[List[StrictStr]] = None
    default_theme: Optional[StrictStr] = None
