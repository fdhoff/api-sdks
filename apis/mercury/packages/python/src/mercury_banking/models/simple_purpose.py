# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class SimplePurpose(ApiModel):
    """SimplePurpose model."""

    additional_info: Optional[StrictStr] = Field(default=None, alias="additionalInfo")
    category: StrictStr
