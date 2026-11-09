# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A01Response200ProDetails(ApiModel):
    """A01Response200ProDetails model."""

    vat_number: Optional[StrictStr] = Field(default=None, alias="VAT_number")
    corporate_name: Optional[StrictStr] = None
    identification_number: Optional[StrictStr] = None
    tax_identification_number: Optional[StrictStr] = None
