# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class RT26RequestReturnsReturnLines(ApiModel):
    """RT26RequestReturnsReturnLines model."""

    compliant: StrictBool
    non_compliance_additional_info: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2000)]] = None
    non_compliance_reason_code: Optional[StrictStr] = None
    order_line_id: StrictStr
