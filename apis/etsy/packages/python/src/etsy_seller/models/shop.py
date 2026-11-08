# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class Shop(ApiModel):
    """Shop model."""

    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shop_name: Optional[StrictStr] = None
    create_date: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    title: Optional[StrictStr] = None
    announcement: Optional[StrictStr] = None
    currency_code: Optional[StrictStr] = None
    is_vacation: Optional[StrictBool] = None
    vacation_message: Optional[StrictStr] = None
    sale_message: Optional[StrictStr] = None
    digital_sale_message: Optional[StrictStr] = None
    update_date: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    updated_timestamp: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    listing_active_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    digital_listing_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    login_name: Optional[StrictStr] = None
    accepts_custom_requests: Optional[StrictBool] = None
    policy_welcome: Optional[StrictStr] = None
    policy_payment: Optional[StrictStr] = None
    policy_shipping: Optional[StrictStr] = None
    policy_refunds: Optional[StrictStr] = None
    policy_additional: Optional[StrictStr] = None
    policy_seller_info: Optional[StrictStr] = None
    policy_update_date: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    policy_has_private_receipt_info: Optional[StrictBool] = None
    has_unstructured_policies: Optional[StrictBool] = None
    policy_privacy: Optional[StrictStr] = None
    vacation_autoreply: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    image_url_760x100: Optional[StrictStr] = None
    num_favorers: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    languages: Optional[List[StrictStr]] = None
    icon_url_fullxfull: Optional[StrictStr] = None
    is_using_structured_policies: Optional[StrictBool] = None
    has_onboarded_structured_policies: Optional[StrictBool] = None
    include_dispute_form_link: Optional[StrictBool] = None
    is_direct_checkout_onboarded: Optional[StrictBool] = None
    is_etsy_payments_onboarded: Optional[StrictBool] = None
    is_calculated_eligible: Optional[StrictBool] = None
    is_opted_in_to_buyer_promise: Optional[StrictBool] = None
    is_shop_us_based: Optional[StrictBool] = None
    transaction_sold_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    shipping_from_country_iso: Optional[StrictStr] = None
    shop_location_country_iso: Optional[StrictStr] = None
    review_count: Optional[StrictInt] = None
    review_average: Optional[float] = None
