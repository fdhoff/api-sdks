# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.charity import Charity
from ebay_sell.inventory.models.extended_producer_responsibility import ExtendedProducerResponsibility
from ebay_sell.inventory.models.listing_policies import ListingPolicies
from ebay_sell.inventory.models.pricing_summary import PricingSummary
from ebay_sell.inventory.models.regulatory import Regulatory
from ebay_sell.inventory.models.tax import Tax
from ebay_sell._runtime import ApiModel


class EbayOfferDetailsWithKeys(ApiModel):
    """EbayOfferDetailsWithKeys model."""

    available_quantity: Optional[StrictInt] = Field(default=None, alias="availableQuantity")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    charity: Optional[Charity] = None
    extended_producer_responsibility: Optional[ExtendedProducerResponsibility] = Field(
        default=None, alias="extendedProducerResponsibility"
    )
    format: Optional[StrictStr] = None
    hide_buyer_details: Optional[StrictBool] = Field(default=None, alias="hideBuyerDetails")
    include_catalog_product_details: Optional[StrictBool] = Field(default=None, alias="includeCatalogProductDetails")
    listing_description: Optional[StrictStr] = Field(default=None, alias="listingDescription")
    listing_duration: Optional[StrictStr] = Field(default=None, alias="listingDuration")
    listing_policies: Optional[ListingPolicies] = Field(default=None, alias="listingPolicies")
    listing_start_date: Optional[StrictStr] = Field(default=None, alias="listingStartDate")
    lot_size: Optional[StrictInt] = Field(default=None, alias="lotSize")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    merchant_location_key: Optional[StrictStr] = Field(default=None, alias="merchantLocationKey")
    pricing_summary: Optional[PricingSummary] = Field(default=None, alias="pricingSummary")
    quantity_limit_per_buyer: Optional[StrictInt] = Field(default=None, alias="quantityLimitPerBuyer")
    regulatory: Optional[Regulatory] = None
    secondary_category_id: Optional[StrictStr] = Field(default=None, alias="secondaryCategoryId")
    sku: Optional[StrictStr] = None
    store_category_names: Optional[List[StrictStr]] = Field(default=None, alias="storeCategoryNames")
    tax: Optional[Tax] = None
