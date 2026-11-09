# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl02_response200_data_entities_order_payment_info import (
    TL02Response200DataEntitiesOrderPaymentInfo,
)
from mirakl_seller.models.tl02_response200_data_entities_order_references import (
    TL02Response200DataEntitiesOrderReferences,
)
from mirakl_seller._runtime import ApiModel


class TL02Response200DataEntitiesOrder(ApiModel):
    """TL02Response200DataEntitiesOrder model."""

    commercial_id: Optional[StrictStr] = None
    creation_date: Optional[datetime] = None
    id: Optional[StrictStr] = None
    payment_info: Optional[TL02Response200DataEntitiesOrderPaymentInfo] = None
    references: Optional[TL02Response200DataEntitiesOrderReferences] = None
