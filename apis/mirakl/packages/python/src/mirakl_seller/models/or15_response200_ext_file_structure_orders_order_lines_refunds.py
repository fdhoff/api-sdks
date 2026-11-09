# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_amount_breakdown import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsAmountBreakdown,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_commission_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsCommissionTaxes,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_eco_contributions import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsEcoContributions,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_fees import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsFees,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_purchase_information import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformation,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_shipping_amount_breakdown import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingAmountBreakdown,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_shipping_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxes,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesRefunds(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesRefunds model."""

    amount: Optional[float] = None
    amount_breakdown: Optional[OR15Response200ExtFileStructureOrdersOrderLinesRefundsAmountBreakdown] = None
    commission_amount: float
    commission_tax_amount: float
    commission_taxes: List[OR15Response200ExtFileStructureOrdersOrderLinesRefundsCommissionTaxes]
    commission_total_amount: float
    created_date: datetime
    eco_contributions: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesRefundsEcoContributions]] = None
    fees: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesRefundsFees]] = None
    id: StrictStr
    order_refund_id: StrictStr
    purchase_information: Optional[OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformation] = None
    quantity: StrictInt
    reason_code: StrictStr
    refund_state: StrictStr
    shipping_amount: Optional[float] = None
    shipping_amount_breakdown: Optional[
        OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingAmountBreakdown
    ] = None
    shipping_taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxes]] = None
    state: StrictStr
    tax_legal_notice: Optional[StrictStr] = None
    taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxes]] = None
    transaction_date: Optional[datetime] = None
    transaction_number: Optional[StrictStr] = None
