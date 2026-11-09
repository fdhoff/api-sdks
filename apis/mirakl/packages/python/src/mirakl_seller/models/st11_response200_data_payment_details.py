# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class ST11Response200DataPaymentDetails(ApiModel):
    """ST11Response200DataPaymentDetails model."""

    customer_debited_date: datetime
    transaction_date: datetime
    transaction_number: Optional[StrictStr] = None
