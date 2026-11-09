# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from mirakl_seller.models.dr12_response200_data_delivery_bill_information import (
    DR12Response200DataDeliveryBillInformation,
)
from mirakl_seller.models.dr12_response200_data_eco_contributions import DR12Response200DataEcoContributions
from mirakl_seller.models.dr12_response200_data_fees_excluding_taxes import DR12Response200DataFeesExcludingTaxes
from mirakl_seller.models.dr12_response200_data_order import DR12Response200DataOrder
from mirakl_seller.models.dr12_response200_data_order_line import DR12Response200DataOrderLine
from mirakl_seller.models.dr12_response200_data_product import DR12Response200DataProduct
from mirakl_seller.models.dr12_response200_data_shipments import DR12Response200DataShipments
from mirakl_seller.models.dr12_response200_data_shipping_from import DR12Response200DataShippingFrom
from mirakl_seller.models.dr12_response200_data_shipping_taxes import DR12Response200DataShippingTaxes
from mirakl_seller.models.dr12_response200_data_shipping_to import DR12Response200DataShippingTo
from mirakl_seller.models.dr12_response200_data_shop import DR12Response200DataShop
from mirakl_seller.models.dr12_response200_data_taxes import DR12Response200DataTaxes
from mirakl_seller._runtime import ApiModel


class DR12Response200Data(ApiModel):
    """DR12Response200Data model."""

    delivery_bill_information: Optional[List[DR12Response200DataDeliveryBillInformation]] = None
    eco_contributions: Optional[List[DR12Response200DataEcoContributions]] = None
    entity_id: StrictStr
    entity_type: StrictStr
    fees_excluding_taxes: Optional[List[DR12Response200DataFeesExcludingTaxes]] = None
    id: StrictStr
    order: Optional[DR12Response200DataOrder] = None
    order_line: Optional[DR12Response200DataOrderLine] = None
    origin_unit_price_excluding_taxes: Optional[float] = None
    origin_unit_price_including_taxes: Optional[float] = None
    price_excluding_taxes: float
    product: Optional[DR12Response200DataProduct] = None
    quantity: StrictInt
    shipments: Optional[List[DR12Response200DataShipments]] = None
    shipping_from: Optional[DR12Response200DataShippingFrom] = None
    shipping_price_excluding_taxes: Optional[float] = None
    shipping_taxes: Optional[List[DR12Response200DataShippingTaxes]] = None
    shipping_to: Optional[DR12Response200DataShippingTo] = None
    shop: DR12Response200DataShop
    tax_legal_notice: Optional[StrictStr] = None
    taxes: List[DR12Response200DataTaxes]
    total_price_including_taxes: float
    unit_price_excluding_taxes: float
