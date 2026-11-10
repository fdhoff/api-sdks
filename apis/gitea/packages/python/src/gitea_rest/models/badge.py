# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class Badge(ApiModel):
    """Badge model."""

    description: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    image_url: Optional[StrictStr] = None
    slug: Optional[StrictStr] = None
