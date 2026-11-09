# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.of21_response200_offers_all_prices import OF21Response200OffersAllPrices
from mirakl_seller.models.of21_response200_offers_applicable_pricing import OF21Response200OffersApplicablePricing
from mirakl_seller.models.of21_response200_offers_discount import OF21Response200OffersDiscount
from mirakl_seller.models.of21_response200_offers_eco_contributions import OF21Response200OffersEcoContributions
from mirakl_seller.models.of21_response200_offers_fulfillment import OF21Response200OffersFulfillment
from mirakl_seller.models.of21_response200_offers_logistic_class import OF21Response200OffersLogisticClass
from mirakl_seller.models.of21_response200_offers_offer_additional_fields import (
    OF21Response200OffersOfferAdditionalFields,
)
from mirakl_seller.models.of21_response200_offers_product_references import OF21Response200OffersProductReferences
from mirakl_seller.models.of21_response200_offers_retail_prices import OF21Response200OffersRetailPrices
from mirakl_seller.models.of21_response200_offers_warehouses import OF21Response200OffersWarehouses
from mirakl_seller._runtime import ApiModel


class OF21Response200Offers(ApiModel):
    """OF21Response200Offers model."""

    active: StrictBool
    all_prices: List[OF21Response200OffersAllPrices]
    allow_quote_requests: Optional[StrictBool] = None
    applicable_pricing: Optional[OF21Response200OffersApplicablePricing] = None
    available_end_date: Optional[datetime] = None
    available_start_date: Optional[datetime] = None
    category_code: StrictStr
    category_label: StrictStr
    channels: List[StrictStr]
    currency_iso_code: StrictStr
    description: StrictStr
    discount: Optional[OF21Response200OffersDiscount] = None
    eco_contributions: Optional[Annotated[List[OF21Response200OffersEcoContributions], Field(max_length=20)]] = None
    favorite_rank: Optional[StrictInt] = None
    fulfillment: OF21Response200OffersFulfillment
    inactivity_reasons: Optional[List[StrictStr]] = None
    internal_description: Optional[StrictStr] = None
    leadtime_to_ship: StrictInt
    logistic_class: OF21Response200OffersLogisticClass
    max_order_quantity: StrictInt
    min_order_quantity: StrictInt
    min_quantity_alert: StrictInt
    min_shipping_price: float
    min_shipping_price_additional: float
    min_shipping_type: StrictStr
    min_shipping_zone: StrictStr
    msrp: Optional[float] = None
    offer_additional_fields: Optional[List[OF21Response200OffersOfferAdditionalFields]] = None
    offer_id: StrictInt
    package_quantity: StrictInt
    price: Optional[float] = None
    price_additional_info: Optional[StrictStr] = None
    product_brand: Optional[StrictStr] = None
    product_description: Optional[StrictStr] = None
    product_references: List[OF21Response200OffersProductReferences]
    product_sku: StrictStr
    product_tax_code: Optional[StrictStr] = None
    product_title: StrictStr
    quantity: StrictInt
    retail_prices: Optional[List[OF21Response200OffersRetailPrices]] = None
    shipping_deadline: datetime
    shop_sku: StrictStr
    state_code: StrictStr
    total_price: Optional[float] = None
    warehouses: Optional[List[OF21Response200OffersWarehouses]] = None
