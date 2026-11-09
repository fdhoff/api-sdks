# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.error_category import ErrorCategory
from ebay_sell.post_order.models.error_parameter import ErrorParameter
from ebay_sell.post_order.models.error_severity import ErrorSeverity
from ebay_sell._runtime import ApiModel


class ErrorData(ApiModel):
    """ErrorData model."""

    category: Optional[ErrorCategory] = None
    domain: Optional[StrictStr] = None
    error_id: Optional[StrictInt] = Field(default=None, alias="errorId")
    http_status_code: Optional[StrictInt] = Field(default=None, alias="httpStatusCode")
    long_message: Optional[StrictStr] = Field(default=None, alias="longMessage")
    message: Optional[StrictStr] = None
    parameter: Optional[List[ErrorParameter]] = None
    severity: Optional[ErrorSeverity] = None
