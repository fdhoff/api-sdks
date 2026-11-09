# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class InternationalWireCorrespondentInfo(ApiModel):
    """InternationalWireCorrespondentInfo model."""

    bank_name: Optional[StrictStr] = Field(default=None, alias="bankName")
    routing_number: Optional[StrictStr] = Field(default=None, alias="routingNumber")
    swift_code: Optional[StrictStr] = Field(default=None, alias="swiftCode")
