# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.of22_response200_all_prices import OF22Response200AllPrices
from mirakl_seller.models.of22_response200_applicable_pricing import OF22Response200ApplicablePricing
from mirakl_seller.models.of22_response200_discount import OF22Response200Discount
from mirakl_seller.models.of22_response200_eco_contributions import OF22Response200EcoContributions
from mirakl_seller.models.of22_response200_fulfillment import OF22Response200Fulfillment
from mirakl_seller.models.of22_response200_logistic_class import OF22Response200LogisticClass
from mirakl_seller.models.of22_response200_offer_additional_fields import OF22Response200OfferAdditionalFields
from mirakl_seller.models.of22_response200_product_references import OF22Response200ProductReferences
from mirakl_seller.models.of22_response200_retail_prices import OF22Response200RetailPrices
from mirakl_seller.models.of22_response200_warehouses import OF22Response200Warehouses
from mirakl_seller._runtime import ApiModel


class OF22Response200(ApiModel):
    """OF22Response200 model."""

    active: StrictBool
    all_prices: List[OF22Response200AllPrices]
    allow_quote_requests: Optional[StrictBool] = None
    applicable_pricing: Optional[OF22Response200ApplicablePricing] = None
    available_end_date: Optional[datetime] = None
    available_start_date: Optional[datetime] = None
    category_code: StrictStr
    category_label: StrictStr
    channels: List[StrictStr]
    currency_iso_code: StrictStr
    description: StrictStr
    discount: Optional[OF22Response200Discount] = None
    eco_contributions: Optional[Annotated[List[OF22Response200EcoContributions], Field(max_length=20)]] = None
    favorite_rank: Optional[StrictInt] = None
    fulfillment: OF22Response200Fulfillment
    inactivity_reasons: Optional[List[StrictStr]] = None
    internal_description: Optional[StrictStr] = None
    leadtime_to_ship: StrictInt
    logistic_class: OF22Response200LogisticClass
    max_order_quantity: StrictInt
    min_order_quantity: StrictInt
    min_quantity_alert: StrictInt
    min_shipping_price: float
    min_shipping_price_additional: float
    min_shipping_type: StrictStr
    min_shipping_zone: StrictStr
    msrp: Optional[float] = None
    offer_additional_fields: Optional[List[OF22Response200OfferAdditionalFields]] = None
    offer_id: StrictInt
    package_quantity: StrictInt
    price: Optional[float] = None
    price_additional_info: Optional[StrictStr] = None
    product_brand: Optional[StrictStr] = None
    product_description: Optional[StrictStr] = None
    product_references: List[OF22Response200ProductReferences]
    product_sku: StrictStr
    product_tax_code: Optional[StrictStr] = None
    product_title: StrictStr
    quantity: StrictInt
    retail_prices: Optional[List[OF22Response200RetailPrices]] = None
    shipping_deadline: datetime
    shop_sku: StrictStr
    state_code: StrictStr
    total_price: Optional[float] = None
    warehouses: Optional[List[OF22Response200Warehouses]] = None
