# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.alert_details import AlertDetails
from ebay_sell._runtime import ApiModel


class Alert(ApiModel):
    """Alert model."""

    alert_type: Optional[StrictStr] = Field(default=None, alias="alertType")
    details: Optional[List[AlertDetails]] = None
