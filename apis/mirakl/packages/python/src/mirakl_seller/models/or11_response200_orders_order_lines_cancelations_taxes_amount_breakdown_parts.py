# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesCancelationsTaxesAmountBreakdownParts(ApiModel):
    """OR11Response200OrdersOrderLinesCancelationsTaxesAmountBreakdownParts model."""

    amount: Annotated[float, Field(ge=0)]
    commissionable: Optional[StrictBool] = None
    debitable_from_customer: Optional[StrictBool] = None
    payable_to_shop: Optional[StrictBool] = None
