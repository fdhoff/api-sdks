# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class TaxIdentifier(ApiModel):
    """TaxIdentifier model."""

    taxpayer_id: Optional[StrictStr] = Field(default=None, alias="taxpayerId")
    tax_identifier_type: Optional[StrictStr] = Field(default=None, alias="taxIdentifierType")
    issuing_country: Optional[StrictStr] = Field(default=None, alias="issuingCountry")
