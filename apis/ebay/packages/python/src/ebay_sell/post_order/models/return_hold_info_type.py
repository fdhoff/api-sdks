# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_hold_status_enum import ReturnHoldStatusEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ReturnHoldInfoType(ApiModel):
    """ReturnHoldInfoType model."""

    hold_creation_date: Optional[Timestamp] = Field(default=None, alias="holdCreationDate")
    hold_reference_id: Optional[StrictStr] = Field(default=None, alias="holdReferenceId")
    hold_release_date: Optional[Timestamp] = Field(default=None, alias="holdReleaseDate")
    hold_status: Optional[ReturnHoldStatusEnum] = Field(default=None, alias="holdStatus")
    hold_transaction_id: Optional[StrictStr] = Field(default=None, alias="holdTransactionId")
