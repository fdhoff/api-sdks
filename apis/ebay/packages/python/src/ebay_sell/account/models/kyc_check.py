# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class KycCheck(ApiModel):
    """KycCheck model."""

    data_required: Optional[StrictStr] = Field(default=None, alias="dataRequired")
    due_date: Optional[StrictStr] = Field(default=None, alias="dueDate")
    remedy_url: Optional[StrictStr] = Field(default=None, alias="remedyUrl")
    alert: Optional[StrictStr] = None
    detail_message: Optional[StrictStr] = Field(default=None, alias="detailMessage")
