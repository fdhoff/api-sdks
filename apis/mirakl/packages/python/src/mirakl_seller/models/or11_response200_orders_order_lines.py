# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations import (
    OR11Response200OrdersOrderLinesCancelations,
)
from mirakl_seller.models.or11_response200_orders_order_lines_commission_taxes import (
    OR11Response200OrdersOrderLinesCommissionTaxes,
)
from mirakl_seller.models.or11_response200_orders_order_lines_discount_campaign import (
    OR11Response200OrdersOrderLinesDiscountCampaign,
)
from mirakl_seller.models.or11_response200_orders_order_lines_eco_contributions import (
    OR11Response200OrdersOrderLinesEcoContributions,
)
from mirakl_seller.models.or11_response200_orders_order_lines_fees import OR11Response200OrdersOrderLinesFees
from mirakl_seller.models.or11_response200_orders_order_lines_measurement import (
    OR11Response200OrdersOrderLinesMeasurement,
)
from mirakl_seller.models.or11_response200_orders_order_lines_order_line_additional_fields import (
    OR11Response200OrdersOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller.models.or11_response200_orders_order_lines_price_amount_breakdown import (
    OR11Response200OrdersOrderLinesPriceAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_product_medias import (
    OR11Response200OrdersOrderLinesProductMedias,
)
from mirakl_seller.models.or11_response200_orders_order_lines_promotions import (
    OR11Response200OrdersOrderLinesPromotions,
)
from mirakl_seller.models.or11_response200_orders_order_lines_purchase_information import (
    OR11Response200OrdersOrderLinesPurchaseInformation,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds import OR11Response200OrdersOrderLinesRefunds
from mirakl_seller.models.or11_response200_orders_order_lines_shipping_from import (
    OR11Response200OrdersOrderLinesShippingFrom,
)
from mirakl_seller.models.or11_response200_orders_order_lines_shipping_price_amount_breakdown import (
    OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_shipping_taxes import (
    OR11Response200OrdersOrderLinesShippingTaxes,
)
from mirakl_seller.models.or11_response200_orders_order_lines_taxes import OR11Response200OrdersOrderLinesTaxes
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLines(ApiModel):
    """OR11Response200OrdersOrderLines model."""

    can_refund: StrictBool
    cancelations: List[OR11Response200OrdersOrderLinesCancelations]
    category_code: StrictStr
    category_label: StrictStr
    commission_fee: float
    commission_rate_vat: float
    commission_taxes: Optional[List[OR11Response200OrdersOrderLinesCommissionTaxes]] = None
    commission_vat: float
    created_date: datetime
    debited_date: Optional[datetime] = None
    description: StrictStr
    discount_campaign: Optional[OR11Response200OrdersOrderLinesDiscountCampaign] = None
    eco_contributions: Optional[List[OR11Response200OrdersOrderLinesEcoContributions]] = None
    fees: Optional[List[OR11Response200OrdersOrderLinesFees]] = None
    last_updated_date: datetime
    measurement: Optional[OR11Response200OrdersOrderLinesMeasurement] = None
    offer_id: StrictInt
    offer_sku: StrictStr
    offer_state_code: StrictStr
    order_line_additional_fields: List[OR11Response200OrdersOrderLinesOrderLineAdditionalFields]
    order_line_id: StrictStr
    order_line_index: StrictInt
    order_line_state: StrictStr
    order_line_state_reason_code: Optional[StrictStr] = None
    order_line_state_reason_label: Optional[StrictStr] = None
    origin_unit_price: Optional[float] = None
    price: float
    price_additional_info: Optional[StrictStr] = None
    price_amount_breakdown: Optional[OR11Response200OrdersOrderLinesPriceAmountBreakdown] = None
    price_unit: float
    product_medias: List[OR11Response200OrdersOrderLinesProductMedias]
    product_shop_sku: Optional[StrictStr] = None
    product_sku: StrictStr
    product_title: StrictStr
    promotions: Optional[List[OR11Response200OrdersOrderLinesPromotions]] = None
    purchase_information: Optional[OR11Response200OrdersOrderLinesPurchaseInformation] = None
    quantity: StrictInt
    received_date: Optional[datetime] = None
    refunds: List[OR11Response200OrdersOrderLinesRefunds]
    shipped_date: Optional[datetime] = None
    shipping_from: Optional[OR11Response200OrdersOrderLinesShippingFrom] = None
    shipping_price: float
    shipping_price_additional_unit: Optional[float] = None
    shipping_price_amount_breakdown: Optional[OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown] = None
    shipping_price_unit: Optional[float] = None
    shipping_taxes: Optional[List[OR11Response200OrdersOrderLinesShippingTaxes]] = None
    tax_legal_notice: Optional[StrictStr] = None
    taxes: Optional[List[OR11Response200OrdersOrderLinesTaxes]] = None
    total_commission: float
    total_price: float
