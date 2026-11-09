# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class RT04Response200ReturnSuccessReturnLinesCompliance(ApiModel):
    """RT04Response200ReturnSuccessReturnLinesCompliance model."""

    compliant: StrictBool
    non_compliance_additional_info: Optional[StrictStr] = None
    non_compliance_reason_code: Optional[StrictStr] = None
