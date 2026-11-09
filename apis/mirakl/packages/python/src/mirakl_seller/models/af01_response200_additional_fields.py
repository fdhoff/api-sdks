# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class AF01Response200AdditionalFields(ApiModel):
    """AF01Response200AdditionalFields model."""

    accepted_values: Optional[List[StrictStr]] = None
    code: StrictStr
    default_value: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    editable: StrictBool
    entity: Optional[StrictStr] = None
    label: StrictStr
    personal_data: Optional[StrictBool] = None
    regex: Optional[StrictStr] = None
    required: StrictBool
    type: StrictStr
