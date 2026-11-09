# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class RefundFeeTypeEnum(str, Enum):
    """Allowed values of RefundFeeTypeEnum."""

    PURCHASE_PRICE = "PURCHASE_PRICE"
    ORIGINAL_SHIPPING = "ORIGINAL_SHIPPING"
    DOMESTIC_SHIPPING = "DOMESTIC_SHIPPING"
    INTERNATIONAL_SHIPPING = "INTERNATIONAL_SHIPPING"
    IMPORT_CHARGE = "IMPORT_CHARGE"
    REFUND_FROM_PAYPAL = "REFUND_FROM_PAYPAL"
    RETURN_SHIPPING = "RETURN_SHIPPING"
    ORDER_ADJUSTMENT = "ORDER_ADJUSTMENT"
    ITEM_IMPORT_TAX = "ITEM_IMPORT_TAX"
    SHIPPING_IMPORT_TAX = "SHIPPING_IMPORT_TAX"
    ITEM_TAX = "ITEM_TAX"
    SHIPPING_TAX = "SHIPPING_TAX"
    OTHER = "OTHER"
