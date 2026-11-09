# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of54_response200_ext_file_structure_eco_contributions import (
    OF54Response200ExtFileStructureEcoContributions,
)
from mirakl_seller.models.of54_response200_ext_file_structure_fulfillment import (
    OF54Response200ExtFileStructureFulfillment,
)
from mirakl_seller.models.of54_response200_ext_file_structure_logistic_class import (
    OF54Response200ExtFileStructureLogisticClass,
)
from mirakl_seller.models.of54_response200_ext_file_structure_measurement import (
    OF54Response200ExtFileStructureMeasurement,
)
from mirakl_seller.models.of54_response200_ext_file_structure_offer_additional_fields import (
    OF54Response200ExtFileStructureOfferAdditionalFields,
)
from mirakl_seller.models.of54_response200_ext_file_structure_ongoing_discount_campaigns import (
    OF54Response200ExtFileStructureOngoingDiscountCampaigns,
)
from mirakl_seller.models.of54_response200_ext_file_structure_prices import OF54Response200ExtFileStructurePrices
from mirakl_seller.models.of54_response200_ext_file_structure_retail_prices import (
    OF54Response200ExtFileStructureRetailPrices,
)
from mirakl_seller.models.of54_response200_ext_file_structure_shipping_types import (
    OF54Response200ExtFileStructureShippingTypes,
)
from mirakl_seller.models.of54_response200_ext_file_structure_warehouses import (
    OF54Response200ExtFileStructureWarehouses,
)
from mirakl_seller._runtime import ApiModel


class OF54Response200ExtFileStructure(ApiModel):
    """OF54Response200ExtFileStructure model."""

    active: Optional[StrictBool] = None
    allow_quote_requests: Optional[StrictBool] = None
    available_end_date: Optional[StrictStr] = None
    available_start_date: Optional[StrictStr] = None
    channels: Optional[List[StrictStr]] = None
    currency_iso_code: Optional[StrictStr] = None
    date_created: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    eco_contributions: Optional[List[OF54Response200ExtFileStructureEcoContributions]] = None
    favorite_rank: Optional[StrictInt] = None
    fulfillment: Optional[OF54Response200ExtFileStructureFulfillment] = None
    is_professional: Optional[StrictBool] = None
    last_updated: Optional[StrictStr] = None
    leadtime_to_ship: Optional[StrictInt] = None
    logistic_class: Optional[OF54Response200ExtFileStructureLogisticClass] = None
    max_order_quantity: Optional[StrictInt] = None
    measurement: Optional[OF54Response200ExtFileStructureMeasurement] = None
    min_order_quantity: Optional[StrictInt] = None
    min_shipping_price: Optional[float] = None
    min_shipping_price_additional: Optional[float] = None
    min_shipping_type: Optional[StrictStr] = None
    min_shipping_zone: Optional[StrictStr] = None
    msrp: Optional[float] = None
    offer_additional_fields: Optional[List[OF54Response200ExtFileStructureOfferAdditionalFields]] = None
    offer_id: Optional[StrictInt] = None
    ongoing_discount_campaigns: Optional[List[OF54Response200ExtFileStructureOngoingDiscountCampaigns]] = None
    package_quantity: Optional[StrictInt] = None
    premium: Optional[StrictBool] = None
    price_additional_info: Optional[StrictStr] = None
    prices: Optional[List[OF54Response200ExtFileStructurePrices]] = None
    product_sku: Optional[StrictStr] = None
    product_tax_code: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = None
    retail_prices: Optional[List[OF54Response200ExtFileStructureRetailPrices]] = None
    shipping_types: Optional[List[OF54Response200ExtFileStructureShippingTypes]] = None
    shop_id: Optional[StrictInt] = None
    shop_name: Optional[StrictStr] = None
    shop_sku: Optional[StrictStr] = None
    state_code: Optional[StrictStr] = None
    warehouses: Optional[List[OF54Response200ExtFileStructureWarehouses]] = None
