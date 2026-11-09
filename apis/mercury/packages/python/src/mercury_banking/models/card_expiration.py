# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class CardExpiration(ApiModel):
    """CardExpiration model."""

    month: Annotated[int, Field(le=12, strict=True, ge=1)]
    year: Annotated[int, Field(le=2999, strict=True, ge=2000)]
