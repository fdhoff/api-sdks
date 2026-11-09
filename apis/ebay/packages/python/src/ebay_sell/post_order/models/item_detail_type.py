# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.relist_status_enum import RelistStatusEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ItemDetailType(ApiModel):
    """ItemDetailType model."""

    ebay_plus_txn: Optional[StrictBool] = Field(default=None, alias="ebayPlusTxn")
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    item_on_hold: Optional[StrictBool] = Field(default=None, alias="itemOnHold")
    listing_site_id: Optional[StrictInt] = Field(default=None, alias="listingSiteId")
    relisted_item_id: Optional[StrictStr] = Field(default=None, alias="relistedItemId")
    relist_status: Optional[RelistStatusEnum] = Field(default=None, alias="relistStatus")
    return_quantity: Optional[StrictInt] = Field(default=None, alias="returnQuantity")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
    transaction_date: Optional[Timestamp] = Field(default=None, alias="transactionDate")
    item_price: Optional[Amount] = Field(default=None, alias="itemPrice")
    item_pic_url: Optional[StrictStr] = Field(default=None, alias="itemPicUrl")
    item_title: Optional[StrictStr] = Field(default=None, alias="itemTitle")
