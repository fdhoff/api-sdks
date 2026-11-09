# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class DR12Response200DataOrderLineAdditionalFields(ApiModel):
    """DR12Response200DataOrderLineAdditionalFields model."""

    code: Optional[Annotated[str, Field(strict=True, max_length=36)]] = None
    type: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
