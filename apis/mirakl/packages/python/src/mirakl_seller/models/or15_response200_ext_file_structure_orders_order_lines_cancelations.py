# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_amount_breakdown import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsAmountBreakdown,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_commission_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsCommissionTaxes,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_eco_contributions import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsEcoContributions,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_fees import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsFees,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_purchase_information import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformation,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_shipping_amount_breakdown import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingAmountBreakdown,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_shipping_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxes,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_cancelations_taxes import (
    OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesCancelations(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesCancelations model."""

    amount: Optional[float] = None
    amount_breakdown: Optional[OR15Response200ExtFileStructureOrdersOrderLinesCancelationsAmountBreakdown] = None
    commission_amount: float
    commission_taxes: List[OR15Response200ExtFileStructureOrdersOrderLinesCancelationsCommissionTaxes]
    commission_total_amount: float
    created_date: datetime
    eco_contributions: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesCancelationsEcoContributions]] = (
        None
    )
    fees: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesCancelationsFees]] = None
    id: StrictStr
    purchase_information: Optional[OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformation] = (
        None
    )
    quantity: Optional[StrictInt] = None
    reason_code: Optional[StrictStr] = None
    shipping_amount: Optional[float] = None
    shipping_amount_breakdown: Optional[
        OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingAmountBreakdown
    ] = None
    shipping_taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxes]] = None
    taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxes]] = None
