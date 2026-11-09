# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt11_response200_data_documents import RT11Response200DataDocuments
from mirakl_seller.models.rt11_response200_data_return_address import RT11Response200DataReturnAddress
from mirakl_seller.models.rt11_response200_data_return_lines import RT11Response200DataReturnLines
from mirakl_seller.models.rt11_response200_data_tracking import RT11Response200DataTracking
from mirakl_seller._runtime import ApiModel


class RT11Response200Data(ApiModel):
    """RT11Response200Data model."""

    date_created: datetime
    description: Optional[StrictStr] = None
    documents: Optional[List[RT11Response200DataDocuments]] = None
    id: StrictStr
    label_url: Optional[StrictStr] = None
    last_updated: datetime
    method_code: StrictStr
    order_commercial_id: StrictStr
    order_id: StrictStr
    reason_code: Optional[StrictStr] = None
    rejection_reason_code: Optional[StrictStr] = None
    return_address: RT11Response200DataReturnAddress
    return_lines: List[RT11Response200DataReturnLines]
    rma: Optional[StrictStr] = None
    state: StrictStr
    tracking: Optional[RT11Response200DataTracking] = None
