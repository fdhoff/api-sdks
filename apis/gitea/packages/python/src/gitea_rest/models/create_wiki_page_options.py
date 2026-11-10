# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreateWikiPageOptions(ApiModel):
    """CreateWikiPageOptions model."""

    content_base64: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
