# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DO01Response200Documents(ApiModel):
    """DO01Response200Documents model."""

    code: StrictStr
    description: StrictStr
    entity: StrictStr
    label: StrictStr
    mime_types: Optional[List[StrictStr]] = None
