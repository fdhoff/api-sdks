# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PayloadDetail(ApiModel):
    """PayloadDetail model."""

    delivery_protocol: Optional[StrictStr] = Field(default=None, alias="deliveryProtocol")
    deprecated: Optional[StrictBool] = None
    format: Optional[List[StrictStr]] = None
    schema_version: Optional[StrictStr] = Field(default=None, alias="schemaVersion")
