# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.error import Error
from backmarket_seller.models.validation_error_response_v3_all_of_errors import ValidationErrorResponseV3AllOfErrors
from backmarket_seller._runtime import ApiModel


class ValidationErrorResponseV3(ApiModel):
    """ValidationErrorResponseV3 model."""

    error: Error
    status: StrictInt
    title: Optional[StrictStr]
    type: Optional[StrictStr]
    request_id: Optional[StrictStr] = Field(default=None, alias="requestId")
    errors: Optional[List[ValidationErrorResponseV3AllOfErrors]] = None
