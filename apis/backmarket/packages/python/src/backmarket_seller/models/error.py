# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class Error(ApiModel):
    """Error model."""

    code: StrictStr
    data: Optional[Dict[str, Any]] = None
    doc_link: Optional[StrictStr] = Field(default=None, alias="docLink")
    message: StrictStr
    target: Optional[StrictStr] = None
