# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class DR12Response200DataFeesCreditCommissionRefundPeriod(ApiModel):
    """DR12Response200DataFeesCreditCommissionRefundPeriod model."""

    date_from: datetime
    date_to: datetime
