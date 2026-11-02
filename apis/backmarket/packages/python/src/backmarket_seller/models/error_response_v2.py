# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from backmarket_seller.models.error import Error
from backmarket_seller._runtime import ApiModel


class ErrorResponseV2(ApiModel):
    """ErrorResponseV2 model."""

    errors: Annotated[List[Error], Field(min_length=1)]
    request_id: Optional[StrictStr] = Field(default=None, alias="requestId")
