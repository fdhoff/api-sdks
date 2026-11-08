# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.local_listing_distance import LocalListingDistance
from ebay_sell._runtime import ApiModel


class MotorsListingPolicy(ApiModel):
    """MotorsListingPolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    deposit_supported: Optional[StrictBool] = Field(default=None, alias="depositSupported")
    ebay_motors_pro_ad_format_enabled: Optional[StrictStr] = Field(default=None, alias="ebayMotorsProAdFormatEnabled")
    ebay_motors_pro_auto_accept_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProAutoAcceptEnabled"
    )
    ebay_motors_pro_auto_decline_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProAutoDeclineEnabled"
    )
    ebay_motors_pro_best_offer_enabled: Optional[StrictStr] = Field(default=None, alias="ebayMotorsProBestOfferEnabled")
    ebay_motors_pro_company_name_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProCompanyNameEnabled"
    )
    ebay_motors_pro_contact_by_address_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProContactByAddressEnabled"
    )
    ebay_motors_pro_contact_by_email_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProContactByEmailEnabled"
    )
    ebay_motors_pro_contact_by_phone_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProContactByPhoneEnabled"
    )
    ebay_motors_pro_counter_offer_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProCounterOfferEnabled"
    )
    ebay_motors_pro_payment_method_check_out_enabled: Optional[StrictStr] = Field(
        default=None, alias="ebayMotorsProPaymentMethodCheckOutEnabled"
    )
    ebay_motors_pro_phone_count: Optional[StrictInt] = Field(default=None, alias="ebayMotorsProPhoneCount")
    ebay_motors_pro_seller_contact_details_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProSellerContactDetailsEnabled"
    )
    ebay_motors_pro_shipping_method_enabled: Optional[StrictBool] = Field(
        default=None, alias="ebayMotorsProShippingMethodEnabled"
    )
    ebay_motors_pro_street_count: Optional[StrictInt] = Field(default=None, alias="ebayMotorsProStreetCount")
    epid_supported: Optional[StrictBool] = Field(default=None, alias="epidSupported")
    k_type_supported: Optional[StrictBool] = Field(default=None, alias="kTypeSupported")
    local_listing_distances: Optional[List[LocalListingDistance]] = Field(default=None, alias="localListingDistances")
    local_market_ad_format_enabled: Optional[StrictStr] = Field(default=None, alias="localMarketAdFormatEnabled")
    local_market_auto_accept_enabled: Optional[StrictBool] = Field(default=None, alias="localMarketAutoAcceptEnabled")
    local_market_auto_decline_enabled: Optional[StrictBool] = Field(default=None, alias="localMarketAutoDeclineEnabled")
    local_market_best_offer_enabled: Optional[StrictStr] = Field(default=None, alias="localMarketBestOfferEnabled")
    local_market_company_name_enabled: Optional[StrictBool] = Field(default=None, alias="localMarketCompanyNameEnabled")
    local_market_contact_by_address_enabled: Optional[StrictBool] = Field(
        default=None, alias="localMarketContactByAddressEnabled"
    )
    local_market_contact_by_email_enabled: Optional[StrictBool] = Field(
        default=None, alias="localMarketContactByEmailEnabled"
    )
    local_market_contact_by_phone_enabled: Optional[StrictBool] = Field(
        default=None, alias="localMarketContactByPhoneEnabled"
    )
    local_market_counter_offer_enabled: Optional[StrictBool] = Field(
        default=None, alias="localMarketCounterOfferEnabled"
    )
    local_market_non_subscription: Optional[StrictBool] = Field(default=None, alias="localMarketNonSubscription")
    local_market_payment_method_check_out_enabled: Optional[StrictStr] = Field(
        default=None, alias="localMarketPaymentMethodCheckOutEnabled"
    )
    local_market_phone_count: Optional[StrictInt] = Field(default=None, alias="localMarketPhoneCount")
    local_market_premium_subscription: Optional[StrictBool] = Field(
        default=None, alias="localMarketPremiumSubscription"
    )
    local_market_regular_subscription: Optional[StrictBool] = Field(
        default=None, alias="localMarketRegularSubscription"
    )
    local_market_seller_contact_details_enabled: Optional[StrictBool] = Field(
        default=None, alias="localMarketSellerContactDetailsEnabled"
    )
    local_market_shipping_method_enabled: Optional[StrictBool] = Field(
        default=None, alias="localMarketShippingMethodEnabled"
    )
    local_market_speciality_subscription: Optional[StrictBool] = Field(
        default=None, alias="localMarketSpecialitySubscription"
    )
    local_market_street_count: Optional[StrictInt] = Field(default=None, alias="localMarketStreetCount")
    max_granular_fitment_count: Optional[StrictInt] = Field(default=None, alias="maxGranularFitmentCount")
    max_item_compatibility: Optional[StrictInt] = Field(default=None, alias="maxItemCompatibility")
    min_item_compatibility: Optional[StrictInt] = Field(default=None, alias="minItemCompatibility")
    non_subscription: Optional[StrictStr] = Field(default=None, alias="nonSubscription")
    premium_subscription: Optional[StrictStr] = Field(default=None, alias="premiumSubscription")
    regular_subscription: Optional[StrictStr] = Field(default=None, alias="regularSubscription")
    seller_provided_title_supported: Optional[StrictBool] = Field(default=None, alias="sellerProvidedTitleSupported")
    speciality_subscription: Optional[StrictStr] = Field(default=None, alias="specialitySubscription")
    vin_supported: Optional[StrictBool] = Field(default=None, alias="vinSupported")
    vrm_supported: Optional[StrictBool] = Field(default=None, alias="vrmSupported")
