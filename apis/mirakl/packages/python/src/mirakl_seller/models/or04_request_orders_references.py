# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR04RequestOrdersReferences(ApiModel):
    """OR04RequestOrdersReferences model."""

    order_reference_for_seller: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = None
