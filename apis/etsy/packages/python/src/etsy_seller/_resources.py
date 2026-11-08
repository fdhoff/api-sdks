# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from etsy_seller._runtime import AsyncTransport, Operation, SyncTransport
from etsy_seller.api import (
    application_api,
    buyer_taxonomy_api,
    economic_operators_api,
    holiday_preferences_api,
    ledger_entries_api,
    listing_files_api,
    listing_images_api,
    listing_inventory_api,
    listing_personalization_api,
    listing_properties_api,
    listing_translations_api,
    listing_variation_images_api,
    listing_videos_api,
    listings_api,
    payments_api,
    processing_profiles_api,
    production_partners_api,
    receipts_api,
    return_policies_api,
    reviews_api,
    seller_taxonomy_api,
    shipping_profiles_api,
    shop_sections_api,
    shops_api,
    transactions_api,
    user_addresses_api,
    users_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        application_api.OPERATIONS,
        buyer_taxonomy_api.OPERATIONS,
        economic_operators_api.OPERATIONS,
        holiday_preferences_api.OPERATIONS,
        ledger_entries_api.OPERATIONS,
        listing_files_api.OPERATIONS,
        listing_images_api.OPERATIONS,
        listing_inventory_api.OPERATIONS,
        listing_personalization_api.OPERATIONS,
        listing_properties_api.OPERATIONS,
        listing_translations_api.OPERATIONS,
        listing_variation_images_api.OPERATIONS,
        listing_videos_api.OPERATIONS,
        listings_api.OPERATIONS,
        payments_api.OPERATIONS,
        processing_profiles_api.OPERATIONS,
        production_partners_api.OPERATIONS,
        receipts_api.OPERATIONS,
        return_policies_api.OPERATIONS,
        reviews_api.OPERATIONS,
        seller_taxonomy_api.OPERATIONS,
        shipping_profiles_api.OPERATIONS,
        shop_sections_api.OPERATIONS,
        shops_api.OPERATIONS,
        transactions_api.OPERATIONS,
        user_addresses_api.OPERATIONS,
        users_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.application = application_api.ApplicationApi(transport)
        self.buyer_taxonomy = buyer_taxonomy_api.BuyerTaxonomyApi(transport)
        self.economic_operators = economic_operators_api.EconomicOperatorsApi(transport)
        self.holiday_preferences = holiday_preferences_api.HolidayPreferencesApi(transport)
        self.ledger_entries = ledger_entries_api.LedgerEntriesApi(transport)
        self.listing_files = listing_files_api.ListingFilesApi(transport)
        self.listing_images = listing_images_api.ListingImagesApi(transport)
        self.listing_inventory = listing_inventory_api.ListingInventoryApi(transport)
        self.listing_personalization = listing_personalization_api.ListingPersonalizationApi(transport)
        self.listing_properties = listing_properties_api.ListingPropertiesApi(transport)
        self.listing_translations = listing_translations_api.ListingTranslationsApi(transport)
        self.listing_variation_images = listing_variation_images_api.ListingVariationImagesApi(transport)
        self.listing_videos = listing_videos_api.ListingVideosApi(transport)
        self.listings = listings_api.ListingsApi(transport)
        self.payments = payments_api.PaymentsApi(transport)
        self.processing_profiles = processing_profiles_api.ProcessingProfilesApi(transport)
        self.production_partners = production_partners_api.ProductionPartnersApi(transport)
        self.receipts = receipts_api.ReceiptsApi(transport)
        self.return_policies = return_policies_api.ReturnPoliciesApi(transport)
        self.reviews = reviews_api.ReviewsApi(transport)
        self.seller_taxonomy = seller_taxonomy_api.SellerTaxonomyApi(transport)
        self.shipping_profiles = shipping_profiles_api.ShippingProfilesApi(transport)
        self.shop_sections = shop_sections_api.ShopSectionsApi(transport)
        self.shops = shops_api.ShopsApi(transport)
        self.transactions = transactions_api.TransactionsApi(transport)
        self.user_addresses = user_addresses_api.UserAddressesApi(transport)
        self.users = users_api.UsersApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.application = application_api.AsyncApplicationApi(transport)
        self.buyer_taxonomy = buyer_taxonomy_api.AsyncBuyerTaxonomyApi(transport)
        self.economic_operators = economic_operators_api.AsyncEconomicOperatorsApi(transport)
        self.holiday_preferences = holiday_preferences_api.AsyncHolidayPreferencesApi(transport)
        self.ledger_entries = ledger_entries_api.AsyncLedgerEntriesApi(transport)
        self.listing_files = listing_files_api.AsyncListingFilesApi(transport)
        self.listing_images = listing_images_api.AsyncListingImagesApi(transport)
        self.listing_inventory = listing_inventory_api.AsyncListingInventoryApi(transport)
        self.listing_personalization = listing_personalization_api.AsyncListingPersonalizationApi(transport)
        self.listing_properties = listing_properties_api.AsyncListingPropertiesApi(transport)
        self.listing_translations = listing_translations_api.AsyncListingTranslationsApi(transport)
        self.listing_variation_images = listing_variation_images_api.AsyncListingVariationImagesApi(transport)
        self.listing_videos = listing_videos_api.AsyncListingVideosApi(transport)
        self.listings = listings_api.AsyncListingsApi(transport)
        self.payments = payments_api.AsyncPaymentsApi(transport)
        self.processing_profiles = processing_profiles_api.AsyncProcessingProfilesApi(transport)
        self.production_partners = production_partners_api.AsyncProductionPartnersApi(transport)
        self.receipts = receipts_api.AsyncReceiptsApi(transport)
        self.return_policies = return_policies_api.AsyncReturnPoliciesApi(transport)
        self.reviews = reviews_api.AsyncReviewsApi(transport)
        self.seller_taxonomy = seller_taxonomy_api.AsyncSellerTaxonomyApi(transport)
        self.shipping_profiles = shipping_profiles_api.AsyncShippingProfilesApi(transport)
        self.shop_sections = shop_sections_api.AsyncShopSectionsApi(transport)
        self.shops = shops_api.AsyncShopsApi(transport)
        self.transactions = transactions_api.AsyncTransactionsApi(transport)
        self.user_addresses = user_addresses_api.AsyncUserAddressesApi(transport)
        self.users = users_api.AsyncUsersApi(transport)
