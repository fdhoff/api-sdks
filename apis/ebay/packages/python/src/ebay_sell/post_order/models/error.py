# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.error_parameter import ErrorParameter
from ebay_sell._runtime import ApiModel


class Error(ApiModel):
    """Error model."""

    category: Optional[StrictStr] = None
    domain: Optional[StrictStr] = None
    error_id: Optional[StrictInt] = Field(default=None, alias="errorId")
    input_ref_ids: Optional[List[StrictStr]] = Field(default=None, alias="inputRefIds")
    long_message: Optional[StrictStr] = Field(default=None, alias="longMessage")
    message: Optional[StrictStr] = None
    output_ref_ids: Optional[List[StrictStr]] = Field(default=None, alias="outputRefIds")
    parameters: Optional[List[ErrorParameter]] = None
    subdomain: Optional[StrictStr] = None
