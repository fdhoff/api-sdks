# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from backmarket_seller._runtime import ApiModel


class ProblemValidationErrorMember(ApiModel):
    """ProblemValidationErrorMember model."""

    type: Annotated[str, Field(min_length=1, strict=True)]
    title: Annotated[str, Field(min_length=1, strict=True)]
    detail: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    target: Annotated[str, Field(min_length=1, strict=True)]
    context: Optional[Dict[str, Any]] = None
