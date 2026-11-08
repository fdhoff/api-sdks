# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ClassifiedAdPolicy(ApiModel):
    """ClassifiedAdPolicy model."""

    ad_format_enabled: Optional[StrictStr] = Field(default=None, alias="adFormatEnabled")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    classified_ad_auto_accept_enabled: Optional[StrictBool] = Field(default=None, alias="classifiedAdAutoAcceptEnabled")
    classified_ad_auto_decline_enabled: Optional[StrictBool] = Field(
        default=None, alias="classifiedAdAutoDeclineEnabled"
    )
    classified_ad_best_offer_enabled: Optional[StrictStr] = Field(default=None, alias="classifiedAdBestOfferEnabled")
    classified_ad_company_name_enabled: Optional[StrictBool] = Field(
        default=None, alias="classifiedAdCompanyNameEnabled"
    )
    classified_ad_contact_by_address_enabled: Optional[StrictBool] = Field(
        default=None, alias="classifiedAdContactByAddressEnabled"
    )
    classified_ad_contact_by_email_enabled: Optional[StrictBool] = Field(
        default=None, alias="classifiedAdContactByEmailEnabled"
    )
    classified_ad_contact_by_phone_enabled: Optional[StrictBool] = Field(
        default=None, alias="classifiedAdContactByPhoneEnabled"
    )
    classified_ad_counter_offer_enabled: Optional[StrictBool] = Field(
        default=None, alias="classifiedAdCounterOfferEnabled"
    )
    classified_ad_payment_method_enabled: Optional[StrictStr] = Field(
        default=None, alias="classifiedAdPaymentMethodEnabled"
    )
    classified_ad_phone_count: Optional[StrictInt] = Field(default=None, alias="classifiedAdPhoneCount")
    classified_ad_shipping_method_enabled: Optional[StrictBool] = Field(
        default=None, alias="classifiedAdShippingMethodEnabled"
    )
    classified_ad_street_count: Optional[StrictInt] = Field(default=None, alias="classifiedAdStreetCount")
    seller_contact_details_enabled: Optional[StrictBool] = Field(default=None, alias="sellerContactDetailsEnabled")
