# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.combined_payment_preferences_type import CombinedPaymentPreferencesType
from ebay_sell.account_v2.models.dispatch_cutoff_time_preferences_type import DispatchCutoffTimePreferencesType
from ebay_sell.account_v2.models.end_of_auction_email_preferences_type import EndOfAuctionEmailPreferencesType
from ebay_sell.account_v2.models.get_items_awaiting_payment_preferences_type import (
    GetItemsAwaitingPaymentPreferencesType,
)
from ebay_sell.account_v2.models.seller_exclude_ship_to_location_preferences_type import (
    SellerExcludeShipToLocationPreferencesType,
)
from ebay_sell.account_v2.models.seller_profile_preferences_type import SellerProfilePreferencesType
from ebay_sell.account_v2.models.shipping_carrier_rate_preferences_type import ShippingCarrierRatePreferencesType
from ebay_sell._runtime import ApiModel


class GetUserPreferencesResponse(ApiModel):
    """GetUserPreferencesResponse model."""

    combined_payment_preferences: Optional[CombinedPaymentPreferencesType] = Field(
        default=None, alias="combinedPaymentPreferences"
    )
    dispatch_cutoff_time_preference: Optional[DispatchCutoffTimePreferencesType] = Field(
        default=None, alias="dispatchCutoffTimePreference"
    )
    email_shipment_tracking_number_preference: Optional[StrictBool] = Field(
        default=None, alias="emailShipmentTrackingNumberPreference"
    )
    end_of_auction_email_preferences: Optional[EndOfAuctionEmailPreferencesType] = Field(
        default=None, alias="endOfAuctionEmailPreferences"
    )
    global_shipping_program_listing_preference: Optional[StrictBool] = Field(
        default=None, alias="globalShippingProgramListingPreference"
    )
    items_awaiting_payment_preferences: Optional[GetItemsAwaitingPaymentPreferencesType] = Field(
        default=None, alias="itemsAwaitingPaymentPreferences"
    )
    offer_global_shipping_program_preference: Optional[StrictBool] = Field(
        default=None, alias="offerGlobalShippingProgramPreference"
    )
    out_of_stock_control_preference: Optional[StrictBool] = Field(default=None, alias="outOfStockControlPreference")
    override_gsp_service_with_intl_service_preference: Optional[StrictBool] = Field(
        default=None, alias="overrideGspServiceWithIntlServicePreference"
    )
    pickup_dropoff_seller_preference: Optional[StrictBool] = Field(default=None, alias="pickupDropoffSellerPreference")
    purchase_reminder_email_preferences: Optional[StrictBool] = Field(
        default=None, alias="purchaseReminderEmailPreferences"
    )
    required_ship_phone_number_preference: Optional[StrictBool] = Field(
        default=None, alias="requiredShipPhoneNumberPreference"
    )
    seller_exclude_ship_to_location_preferences: Optional[SellerExcludeShipToLocationPreferencesType] = Field(
        default=None, alias="sellerExcludeShipToLocationPreferences"
    )
    seller_profile_preferences: Optional[SellerProfilePreferencesType] = Field(
        default=None, alias="sellerProfilePreferences"
    )
    shipping_carrier_rate_preferences: Optional[ShippingCarrierRatePreferencesType] = Field(
        default=None, alias="shippingCarrierRatePreferences"
    )
