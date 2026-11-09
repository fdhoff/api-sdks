# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.dr12_response200_data import DR12Response200Data
from mirakl_seller.models.dr12_response200_data_delivery_bill_information import (
    DR12Response200DataDeliveryBillInformation,
)
from mirakl_seller.models.dr12_response200_data_eco_contributions import DR12Response200DataEcoContributions
from mirakl_seller.models.dr12_response200_data_fees_credit_one_off_references import (
    DR12Response200DataFeesCreditOneOffReferences,
)
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


class DR12Response200DataFeesCreditOneOff(DR12Response200Data):
    """DR12Response200DataFeesCreditOneOff model."""

    description: StrictStr
    operation_date: Optional[date] = None
    references: Annotated[List[DR12Response200DataFeesCreditOneOffReferences], Field(min_length=0, max_length=1)]
