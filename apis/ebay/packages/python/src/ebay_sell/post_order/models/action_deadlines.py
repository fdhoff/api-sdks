# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ActionDeadlines(ApiModel):
    """ActionDeadlines model."""

    days_for_buyer_to_provide_proof_of_shipment: Optional[StrictInt] = Field(
        default=None, alias="daysForBuyerToProvideProofOfShipment"
    )
    days_to_expire_without_response: Optional[StrictInt] = Field(default=None, alias="daysToExpireWithoutResponse")
    days_to_expire_with_response: Optional[StrictInt] = Field(default=None, alias="daysToExpireWithResponse")
    days_to_return_item: Optional[StrictInt] = Field(default=None, alias="daysToReturnItem")
    max_days_to_file_claim: Optional[StrictInt] = Field(default=None, alias="maxDaysToFileClaim")
