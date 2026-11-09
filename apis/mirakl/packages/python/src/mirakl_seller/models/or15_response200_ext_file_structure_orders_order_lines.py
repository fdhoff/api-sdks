# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelations,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_commission_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesCommissionTaxes,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_discount_campaign import (
    OR15Response200ExtFileStructureOrdersOrderLinesDiscountCampaign,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_eco_contributions import (
    OR15Response200ExtFileStructureOrdersOrderLinesEcoContributions,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_fees import (
    OR15Response200ExtFileStructureOrdersOrderLinesFees,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_measurement import (
    OR15Response200ExtFileStructureOrdersOrderLinesMeasurement,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_order_line_additional_fields import (
    OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_price_amount_breakdown import (
    OR15Response200ExtFileStructureOrdersOrderLinesPriceAmountBreakdown,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_product_medias import (
    OR15Response200ExtFileStructureOrdersOrderLinesProductMedias,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_promotions import (
    OR15Response200ExtFileStructureOrdersOrderLinesPromotions,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_purchase_information import (
    OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformation,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefunds,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_from import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingFrom,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_price_amount_breakdown import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdown,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxes,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLines(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLines model."""

    can_refund: StrictBool
    cancelations: List[OR15Response200ExtFileStructureOrdersOrderLinesCancelations]
    category_code: StrictStr
    category_label: StrictStr
    commission_fee: float
    commission_rate_vat: float
    commission_taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesCommissionTaxes]] = None
    commission_vat: float
    created_date: datetime
    debited_date: Optional[datetime] = None
    description: StrictStr
    discount_campaign: Optional[OR15Response200ExtFileStructureOrdersOrderLinesDiscountCampaign] = None
    eco_contributions: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesEcoContributions]] = None
    fees: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesFees]] = None
    last_updated_date: datetime
    measurement: Optional[OR15Response200ExtFileStructureOrdersOrderLinesMeasurement] = None
    offer_id: StrictInt
    offer_sku: StrictStr
    offer_state_code: StrictStr
    order_line_additional_fields: List[OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields]
    order_line_id: StrictStr
    order_line_index: StrictInt
    order_line_state: StrictStr
    order_line_state_reason_code: Optional[StrictStr] = None
    order_line_state_reason_label: Optional[StrictStr] = None
    origin_unit_price: Optional[float] = None
    price: float
    price_additional_info: Optional[StrictStr] = None
    price_amount_breakdown: Optional[OR15Response200ExtFileStructureOrdersOrderLinesPriceAmountBreakdown] = None
    price_unit: float
    product_medias: List[OR15Response200ExtFileStructureOrdersOrderLinesProductMedias]
    product_shop_sku: Optional[StrictStr] = None
    product_sku: StrictStr
    product_title: StrictStr
    promotions: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesPromotions]] = None
    purchase_information: Optional[OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformation] = None
    quantity: StrictInt
    received_date: Optional[datetime] = None
    refunds: List[OR15Response200ExtFileStructureOrdersOrderLinesRefunds]
    shipped_date: Optional[datetime] = None
    shipping_from: Optional[OR15Response200ExtFileStructureOrdersOrderLinesShippingFrom] = None
    shipping_price: float
    shipping_price_additional_unit: Optional[float] = None
    shipping_price_amount_breakdown: Optional[
        OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdown
    ] = None
    shipping_price_unit: Optional[float] = None
    shipping_taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxes]] = None
    tax_legal_notice: Optional[StrictStr] = None
    taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesTaxes]] = None
    total_commission: float
    total_price: float
