# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.dr12_response200_data_order_additional_fields import DR12Response200DataOrderAdditionalFields
from mirakl_seller.models.dr12_response200_data_order_transaction_info import DR12Response200DataOrderTransactionInfo
from mirakl_seller._runtime import ApiModel


class DR12Response200DataOrder(ApiModel):
    """DR12Response200DataOrder model."""

    additional_fields: Optional[Annotated[List[DR12Response200DataOrderAdditionalFields], Field(min_length=0)]] = None
    commercial_id: Optional[StrictStr] = None
    date_created: Optional[datetime] = None
    id: StrictStr
    reference_for_customer: Optional[StrictStr] = None
    reference_for_seller: Optional[StrictStr] = None
    transaction_info: Optional[DR12Response200DataOrderTransactionInfo] = None
