# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl02_response200_data_entities_fee_cancelations import (
    TL02Response200DataEntitiesFeeCancelations,
)
from mirakl_seller.models.tl02_response200_data_entities_fee_refunds import TL02Response200DataEntitiesFeeRefunds
from mirakl_seller._runtime import ApiModel


class TL02Response200DataEntitiesFee(ApiModel):
    """TL02Response200DataEntitiesFee model."""

    cancelations: Optional[List[TL02Response200DataEntitiesFeeCancelations]] = None
    code: Optional[StrictStr] = None
    refunds: Optional[List[TL02Response200DataEntitiesFeeRefunds]] = None
