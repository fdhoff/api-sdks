# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.p11_response200_products_offers_all_prices import P11Response200ProductsOffersAllPrices
from mirakl_seller.models.p11_response200_products_offers_applicable_pricing import (
    P11Response200ProductsOffersApplicablePricing,
)
from mirakl_seller.models.p11_response200_products_offers_discount import P11Response200ProductsOffersDiscount
from mirakl_seller.models.p11_response200_products_offers_eco_contributions import (
    P11Response200ProductsOffersEcoContributions,
)
from mirakl_seller.models.p11_response200_products_offers_logistic_class import (
    P11Response200ProductsOffersLogisticClass,
)
from mirakl_seller.models.p11_response200_products_offers_offer_additional_fields import (
    P11Response200ProductsOffersOfferAdditionalFields,
)
from mirakl_seller.models.p11_response200_products_offers_retail_prices import P11Response200ProductsOffersRetailPrices
from mirakl_seller.models.p11_response200_products_offers_shipping_types import (
    P11Response200ProductsOffersShippingTypes,
)
from mirakl_seller._runtime import ApiModel


class P11Response200ProductsOffers(ApiModel):
    """P11Response200ProductsOffers model."""

    active: StrictBool
    all_prices: List[P11Response200ProductsOffersAllPrices]
    allow_quote_requests: Optional[StrictBool] = None
    applicable_pricing: Optional[P11Response200ProductsOffersApplicablePricing] = None
    available_end_date: Optional[datetime] = None
    available_start_date: Optional[datetime] = None
    channels: List[StrictStr]
    currency_iso_code: StrictStr
    description: StrictStr
    discount: Optional[P11Response200ProductsOffersDiscount] = None
    eco_contributions: Optional[Annotated[List[P11Response200ProductsOffersEcoContributions], Field(max_length=20)]] = (
        None
    )
    favorite_rank: Optional[StrictInt] = None
    inactivity_reasons: Optional[List[StrictStr]] = None
    is_professional: StrictBool
    leadtime_to_ship: StrictInt
    logistic_class: P11Response200ProductsOffersLogisticClass
    min_quantity_alert: StrictInt
    min_shipping_price: float
    min_shipping_price_additional: float
    min_shipping_type: StrictStr
    min_shipping_zone: StrictStr
    msrp: Optional[float] = None
    nb_evaluation: StrictInt
    offer_additional_fields: Optional[List[P11Response200ProductsOffersOfferAdditionalFields]] = None
    offer_id: StrictInt
    premium: StrictBool
    price: Optional[float] = None
    price_additional_info: Optional[StrictStr] = None
    quantity: StrictInt
    retail_prices: Optional[List[P11Response200ProductsOffersRetailPrices]] = None
    shipping_deadline: datetime
    shipping_types: Optional[List[P11Response200ProductsOffersShippingTypes]] = None
    shop_grade: float
    shop_id: StrictInt
    shop_name: StrictStr
    state_code: StrictStr
    total_price: Optional[float] = None
