# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.item_detail_type import ItemDetailType
from ebay_sell.post_order.models.marketplace_id_enum import MarketplaceIdEnum
from ebay_sell.post_order.models.refund_info_type import RefundInfoType
from ebay_sell.post_order.models.ret_money_movement_detail_type import RetMoneyMovementDetailType
from ebay_sell.post_order.models.return_address_type import ReturnAddressType
from ebay_sell.post_order.models.return_close_info_type import ReturnCloseInfoType
from ebay_sell.post_order.models.return_file_type import ReturnFileType
from ebay_sell.post_order.models.return_hold_info_type import ReturnHoldInfoType
from ebay_sell.post_order.models.return_payout_recoup_info_type import ReturnPayoutRecoupInfoType
from ebay_sell.post_order.models.return_response_history_type import ReturnResponseHistoryType
from ebay_sell.post_order.models.shipment_type import ShipmentType
from ebay_sell._runtime import ApiModel


class ReturnDetailType(ApiModel):
    """ReturnDetailType model."""

    buyer_address: Optional[ReturnAddressType] = Field(default=None, alias="buyerAddress")
    buyer_login_name: Optional[StrictStr] = Field(default=None, alias="buyerLoginName")
    close_info: Optional[ReturnCloseInfoType] = Field(default=None, alias="closeInfo")
    files: Optional[List[ReturnFileType]] = None
    hold_info: Optional[ReturnHoldInfoType] = Field(default=None, alias="holdInfo")
    item_detail: Optional[ItemDetailType] = Field(default=None, alias="itemDetail")
    marketplace_id: Optional[MarketplaceIdEnum] = Field(default=None, alias="marketplaceId")
    money_movement_info: Optional[List[RetMoneyMovementDetailType]] = Field(default=None, alias="moneyMovementInfo")
    payout_recoup_info: Optional[ReturnPayoutRecoupInfoType] = Field(default=None, alias="payoutRecoupInfo")
    refund_info: Optional[RefundInfoType] = Field(default=None, alias="refundInfo")
    replacement_shipment_info: Optional[ShipmentType] = Field(default=None, alias="replacementShipmentInfo")
    response_history: Optional[List[ReturnResponseHistoryType]] = Field(default=None, alias="responseHistory")
    return_shipment_info: Optional[ShipmentType] = Field(default=None, alias="returnShipmentInfo")
    return_content_on_hold: Optional[StrictBool] = Field(default=None, alias="returnContentOnHold")
    rma_number: Optional[StrictStr] = Field(default=None, alias="RMANumber")
    seller_address: Optional[ReturnAddressType] = Field(default=None, alias="sellerAddress")
    seller_login_name: Optional[StrictStr] = Field(default=None, alias="sellerLoginName")
