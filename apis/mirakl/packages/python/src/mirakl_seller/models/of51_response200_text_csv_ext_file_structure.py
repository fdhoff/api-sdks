# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OF51Response200TextCsvExtFileStructure(ApiModel):
    """OF51Response200TextCsvExtFileStructure model."""

    active: Optional[StrictBool] = None
    allow_quote_requests: Optional[StrictBool] = Field(default=None, alias="allow-quote-requests")
    available_end_date: Optional[StrictStr] = Field(default=None, alias="available-end-date")
    available_start_date: Optional[StrictStr] = Field(default=None, alias="available-start-date")
    channels: Optional[StrictStr] = None
    currency_iso_code: Optional[StrictStr] = Field(default=None, alias="currency-iso-code")
    date_created: Optional[StrictStr] = Field(default=None, alias="date-created")
    deleted: Optional[StrictBool] = None
    delivery_time_earliest_days_zone_cod_emethod_code: Optional[StrictStr] = Field(
        default=None, alias="delivery-time-earliest-days[zone=<CODE>,method=<CODE>]"
    )
    delivery_time_latest_days_zone_cod_emethod_code: Optional[StrictStr] = Field(
        default=None, alias="delivery-time-latest-days[zone=<CODE>,method=<CODE>]"
    )
    description: Optional[StrictStr] = None
    discount_end_date: Optional[StrictStr] = Field(default=None, alias="discount-end-date")
    discount_end_date_channelchannel_code: Optional[StrictStr] = Field(
        default=None, alias="discount-end-date[channel=<channelCode>]"
    )
    discount_price: Optional[float] = Field(default=None, alias="discount-price")
    discount_price_channelchannel_code: Optional[float] = Field(
        default=None, alias="discount-price[channel=<channelCode>]"
    )
    discount_ranges: Optional[StrictStr] = Field(default=None, alias="discount-ranges")
    discount_ranges_channelchannel_code: Optional[StrictStr] = Field(
        default=None, alias="discount-ranges[channel=<channelCode>]"
    )
    discount_retail_price: Optional[float] = Field(default=None, alias="discount-retail-price")
    discount_retail_price_end_date: Optional[StrictStr] = Field(default=None, alias="discount-retail-price-end-date")
    discount_retail_price_start_date: Optional[StrictStr] = Field(
        default=None, alias="discount-retail-price-start-date"
    )
    discount_start_date: Optional[StrictStr] = Field(default=None, alias="discount-start-date")
    discount_start_date_channelchannel_code: Optional[StrictStr] = Field(
        default=None, alias="discount-start-date[channel=<channelCode>]"
    )
    eco_contribution_amount_epr_category_code: Optional[float] = Field(
        default=None, alias="eco-contribution-amount[EPR category code]"
    )
    favorite_rank: Optional[StrictInt] = Field(default=None, alias="favorite-rank")
    fulfillment_center_code: Optional[StrictStr] = Field(default=None, alias="fulfillment-center-code")
    last_updated: Optional[StrictStr] = Field(default=None, alias="last-updated")
    leadtime_to_ship: Optional[StrictInt] = Field(default=None, alias="leadtime-to-ship")
    logistic_class: Optional[StrictStr] = Field(default=None, alias="logistic-class")
    max_order_quantity: Optional[StrictInt] = Field(default=None, alias="max-order-quantity")
    measurement_units: Optional[StrictStr] = Field(default=None, alias="measurement-units")
    min_order_quantity: Optional[StrictInt] = Field(default=None, alias="min-order-quantity")
    min_shipping_price: Optional[float] = Field(default=None, alias="min-shipping-price")
    min_shipping_price_additional: Optional[float] = Field(default=None, alias="min-shipping-price-additional")
    min_shipping_type: Optional[StrictStr] = Field(default=None, alias="min-shipping-type")
    min_shipping_zone: Optional[StrictStr] = Field(default=None, alias="min-shipping-zone")
    msrp: Optional[float] = None
    offer_id: Optional[StrictInt] = Field(default=None, alias="offer-id")
    ongoing_discount_campaigns: Optional[StrictStr] = Field(default=None, alias="ongoing-discount-campaigns")
    origin_price: Optional[float] = Field(default=None, alias="origin-price")
    origin_price_channelchannel_code: Optional[float] = Field(default=None, alias="origin-price[channel=<channelCode>]")
    origin_retail_price: Optional[float] = Field(default=None, alias="origin-retail-price")
    package_quantity: Optional[StrictInt] = Field(default=None, alias="package-quantity")
    premium: Optional[StrictBool] = None
    price: Optional[float] = None
    price_additional_info: Optional[StrictStr] = Field(default=None, alias="price-additional-info")
    price_ranges: Optional[StrictStr] = Field(default=None, alias="price-ranges")
    price_ranges_channelchannel_code: Optional[StrictStr] = Field(
        default=None, alias="price-ranges[channel=<channelCode>]"
    )
    price_channelchannel_code: Optional[float] = Field(default=None, alias="price[channel=<channelCode>]")
    producer_id_epr_category_code: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None, alias="producer-id[EPR category code]"
    )
    product_sku: Optional[StrictStr] = Field(default=None, alias="product-sku")
    product_tax_code: Optional[StrictStr] = Field(default=None, alias="product-tax-code")
    professional: Optional[StrictBool] = None
    quantity: Optional[StrictInt] = None
    retail_price: Optional[float] = Field(default=None, alias="retail-price")
    shipping_price_type_zone_cod_emethod_code: Optional[StrictStr] = Field(
        default=None, alias="shipping-price-type[zone=<CODE>,method=<CODE>]"
    )
    shipping_price_zone_cod_emethod_code: Optional[float] = Field(
        default=None, alias="shipping-price[zone=<CODE>,method=<CODE>]"
    )
    shop_id: Optional[StrictInt] = Field(default=None, alias="shop-id")
    shop_name: Optional[StrictStr] = Field(default=None, alias="shop-name")
    shop_sku: Optional[StrictStr] = Field(default=None, alias="shop-sku")
    state_code: Optional[StrictStr] = Field(default=None, alias="state-code")
    total_price: Optional[float] = Field(default=None, alias="total-price")
