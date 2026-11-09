# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class CaseSummaryType(ApiModel):
    """CaseSummaryType model."""

    buyer: Optional[StrictStr] = None
    case_id: Optional[StrictInt] = Field(default=None, alias="caseId")
    case_status_enum: Optional[StrictStr] = Field(default=None, alias="caseStatusEnum")
    claim_amount: Optional[Amount] = Field(default=None, alias="claimAmount")
    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    item_id: Optional[StrictInt] = Field(default=None, alias="itemId")
    last_modified_date: Optional[Timestamp] = Field(default=None, alias="lastModifiedDate")
    respond_by_date: Optional[Timestamp] = Field(default=None, alias="respondByDate")
    seller: Optional[StrictStr] = None
    transaction_id: Optional[StrictInt] = Field(default=None, alias="transactionId")
