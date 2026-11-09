# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR51Response200Reply(ApiModel):
    """OR51Response200Reply model."""

    comment: Annotated[str, Field(min_length=1, strict=True, max_length=1000)]
    var_date: datetime = Field(alias="date")
    type: StrictStr
