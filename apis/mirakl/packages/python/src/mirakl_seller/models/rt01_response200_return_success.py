# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt01_response200_return_success_documents import RT01Response200ReturnSuccessDocuments
from mirakl_seller.models.rt01_response200_return_success_return_address import (
    RT01Response200ReturnSuccessReturnAddress,
)
from mirakl_seller.models.rt01_response200_return_success_return_lines import RT01Response200ReturnSuccessReturnLines
from mirakl_seller.models.rt01_response200_return_success_tracking import RT01Response200ReturnSuccessTracking
from mirakl_seller._runtime import ApiModel


class RT01Response200ReturnSuccess(ApiModel):
    """RT01Response200ReturnSuccess model."""

    date_created: datetime
    description: Optional[StrictStr] = None
    documents: Optional[List[RT01Response200ReturnSuccessDocuments]] = None
    id: StrictStr
    label_url: Optional[StrictStr] = None
    last_updated: datetime
    method_code: StrictStr
    order_commercial_id: StrictStr
    order_id: StrictStr
    reason_code: Optional[StrictStr] = None
    rejection_reason_code: Optional[StrictStr] = None
    return_address: RT01Response200ReturnSuccessReturnAddress
    return_lines: List[RT01Response200ReturnSuccessReturnLines]
    rma: Optional[StrictStr] = None
    state: StrictStr
    tracking: Optional[RT01Response200ReturnSuccessTracking] = None
