# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_taxes_amount_breakdown import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesAmountBreakdown,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_taxes_purchase_tax import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesPurchaseTax,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxes(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxes model."""

    amount: float
    amount_breakdown: Optional[OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesAmountBreakdown] = None
    code: StrictStr
    purchase_tax: Optional[OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesPurchaseTax] = None
    rate: Optional[float] = None
    tax_calculation_rule: StrictStr
