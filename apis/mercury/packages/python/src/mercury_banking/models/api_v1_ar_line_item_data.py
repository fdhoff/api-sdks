# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class ApiV1ArLineItemData(ApiModel):
    """ApiV1ArLineItemData model."""

    name: StrictStr
    quantity: float
    sales_tax_rate: Optional[float] = Field(default=None, alias="salesTaxRate")
    unit_price: Annotated[float, Field(multiple_of=0.01)] = Field(alias="unitPrice")
