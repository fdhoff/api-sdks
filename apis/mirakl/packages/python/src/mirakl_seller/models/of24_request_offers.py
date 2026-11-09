# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of24_request_offers_all_prices import OF24RequestOffersAllPrices
from mirakl_seller.models.of24_request_offers_discount import OF24RequestOffersDiscount
from mirakl_seller.models.of24_request_offers_eco_contributions import OF24RequestOffersEcoContributions
from mirakl_seller.models.of24_request_offers_offer_additional_fields import OF24RequestOffersOfferAdditionalFields
from mirakl_seller.models.of24_request_offers_retail_prices import OF24RequestOffersRetailPrices
from mirakl_seller._runtime import ApiModel


class OF24RequestOffers(ApiModel):
    """OF24RequestOffers model."""

    all_prices: Optional[List[OF24RequestOffersAllPrices]] = None
    allow_quote_requests: Optional[StrictBool] = None
    available_ended: Optional[StrictStr] = None
    available_started: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    discount: Optional[OF24RequestOffersDiscount] = None
    eco_contributions: Optional[List[OF24RequestOffersEcoContributions]] = None
    internal_description: Optional[StrictStr] = None
    leadtime_to_ship: Optional[StrictInt] = None
    logistic_class: Optional[StrictStr] = None
    max_order_quantity: Optional[StrictInt] = None
    min_order_quantity: Optional[StrictInt] = None
    min_quantity_alert: Optional[StrictInt] = None
    msrp: Optional[float] = None
    offer_additional_fields: Optional[List[OF24RequestOffersOfferAdditionalFields]] = None
    package_quantity: Optional[StrictInt] = None
    price: float
    price_additional_info: Optional[StrictStr] = None
    pricing_unit: Optional[StrictStr] = None
    product_id: StrictStr
    product_id_type: StrictStr
    product_tax_code: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = None
    retail_prices: Optional[List[OF24RequestOffersRetailPrices]] = None
    shop_sku: StrictStr
    state_code: StrictStr
    update_delete: StrictStr
