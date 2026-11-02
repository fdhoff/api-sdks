# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class Category3(ApiModel):
    """Category3 model."""

    category_name: Optional[StrictStr] = None
    parent: Optional[Category3] = None


Category3.model_rebuild(raise_errors=False)
