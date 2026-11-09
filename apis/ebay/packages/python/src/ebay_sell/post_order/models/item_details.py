# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell._runtime import ApiModel


class ItemDetails(ApiModel):
    """ItemDetails model."""

    item_on_hold: Optional[StrictBool] = Field(default=None, alias="itemOnHold")
    item_picture_url: Optional[StrictStr] = Field(default=None, alias="itemPictureUrl")
    item_price: Optional[Amount] = Field(default=None, alias="itemPrice")
    item_title: Optional[StrictStr] = Field(default=None, alias="itemTitle")
    view_purchased_item_url: Optional[StrictStr] = Field(default=None, alias="viewPurchasedItemUrl")
