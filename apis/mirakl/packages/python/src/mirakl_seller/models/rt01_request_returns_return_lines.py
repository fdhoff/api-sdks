# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class RT01RequestReturnsReturnLines(ApiModel):
    """RT01RequestReturnsReturnLines model."""

    order_line_id: StrictStr
    quantity: Annotated[int, Field(strict=True, ge=1)]
    reason_code: StrictStr
