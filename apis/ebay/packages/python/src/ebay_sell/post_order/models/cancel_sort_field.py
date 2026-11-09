# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class CancelSortField(ApiModel):
    """CancelSortField model."""

    ascending: Optional[StrictBool] = None
    enum_value: Optional[Dict[str, Any]] = Field(default=None, alias="enumValue")
    var_field: Optional[StrictStr] = Field(default=None, alias="field")
