# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller._runtime import ApiModel


class TransactionVariations(ApiModel):
    """TransactionVariations model."""

    property_id: Optional[StrictInt] = None
    value_id: Optional[StrictInt] = None
    formatted_name: Optional[StrictStr] = None
    formatted_value: Optional[StrictStr] = None
    question_id: Optional[StrictInt] = None
    mime_type: Optional[StrictStr] = None
