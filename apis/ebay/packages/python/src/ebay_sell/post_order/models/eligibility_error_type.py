# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class EligibilityErrorType(ApiModel):
    """EligibilityErrorType model."""

    code: Optional[StrictStr] = None
    content: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
