# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.iv01_response200_invoices_details_taxes import IV01Response200InvoicesDetailsTaxes
from mirakl_seller._runtime import ApiModel


class IV01Response200InvoicesDetails(ApiModel):
    """IV01Response200InvoicesDetails model."""

    amount_excl_taxes: Optional[float] = None
    description: Optional[StrictStr] = None
    operation_date: Optional[datetime] = None
    order_id: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = None
    taxes: Optional[List[IV01Response200InvoicesDetailsTaxes]] = None
