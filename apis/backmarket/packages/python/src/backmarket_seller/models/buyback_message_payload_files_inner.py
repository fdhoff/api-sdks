# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from backmarket_seller._runtime import ApiModel


class BuybackMessagePayloadFilesInner(ApiModel):
    """BuybackMessagePayloadFilesInner model."""

    name: Annotated[str, Field(min_length=1, strict=True)]
    content: Annotated[str, Field(min_length=1, strict=True)]
