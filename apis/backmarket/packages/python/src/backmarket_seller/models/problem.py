# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from backmarket_seller._runtime import ApiModel


class Problem(ApiModel):
    """Problem model."""

    type: StrictStr
    title: StrictStr
    status: Annotated[int, Field(le=599, strict=True, ge=100)]
    detail: Optional[StrictStr] = None
    instance: Optional[StrictStr] = None
