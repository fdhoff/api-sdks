# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller.models.shop_receipt_shipment import ShopReceiptShipment
from etsy_seller.models.shop_receipt_transaction import ShopReceiptTransaction
from etsy_seller.models.shop_refund import ShopRefund
from etsy_seller._runtime import ApiModel


class ShopReceipt(ApiModel):
    """ShopReceipt model."""

    receipt_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    receipt_type: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    seller_user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    seller_email: Optional[StrictStr] = None
    buyer_user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    buyer_email: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    first_line: Optional[StrictStr] = None
    second_line: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    zip: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    formatted_address: Optional[StrictStr] = None
    country_iso: Optional[StrictStr] = None
    payment_method: Optional[StrictStr] = None
    payment_email: Optional[StrictStr] = None
    message_from_seller: Optional[StrictStr] = None
    message_from_buyer: Optional[StrictStr] = None
    message_from_payment: Optional[StrictStr] = None
    is_paid: Optional[StrictBool] = None
    is_shipped: Optional[StrictBool] = None
    create_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    update_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    updated_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    is_gift: Optional[StrictBool] = None
    gift_message: Optional[StrictStr] = None
    gift_sender: Optional[StrictStr] = None
    grandtotal: Optional[Money] = None
    subtotal: Optional[Money] = None
    total_price: Optional[Money] = None
    total_shipping_cost: Optional[Money] = None
    total_tax_cost: Optional[Money] = None
    total_vat_cost: Optional[Money] = None
    discount_amt: Optional[Money] = None
    gift_wrap_price: Optional[Money] = None
    shipments: Optional[List[ShopReceiptShipment]] = None
    transactions: Optional[List[ShopReceiptTransaction]] = None
    refunds: Optional[List[ShopRefund]] = None
