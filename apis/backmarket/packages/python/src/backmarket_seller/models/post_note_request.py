# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from backmarket_seller._runtime import ApiModel


class PostNoteRequest(ApiModel):
    """PostNoteRequest model."""

    note: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
