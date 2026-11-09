# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR42Request(ApiModel):
    """OR42Request model."""

    body: Annotated[str, Field(min_length=3, strict=True, max_length=50000)]
    document_ids: Optional[List[StrictInt]] = None
    subject: Annotated[str, Field(min_length=3, strict=True, max_length=200)]
    to_customer: StrictBool
    to_operator: StrictBool
    to_shop: StrictBool
