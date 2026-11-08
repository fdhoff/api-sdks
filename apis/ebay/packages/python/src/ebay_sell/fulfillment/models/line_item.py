# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell.fulfillment.models.applied_promotion import AppliedPromotion
from ebay_sell.fulfillment.models.delivery_cost import DeliveryCost
from ebay_sell.fulfillment.models.ebay_collect_and_remit_tax import EbayCollectAndRemitTax
from ebay_sell.fulfillment.models.ebay_collected_charges import EbayCollectedCharges
from ebay_sell.fulfillment.models.gift_details import GiftDetails
from ebay_sell.fulfillment.models.item_location import ItemLocation
from ebay_sell.fulfillment.models.line_item_fulfillment_instructions import LineItemFulfillmentInstructions
from ebay_sell.fulfillment.models.line_item_properties import LineItemProperties
from ebay_sell.fulfillment.models.line_item_refund import LineItemRefund
from ebay_sell.fulfillment.models.linked_order_line_item import LinkedOrderLineItem
from ebay_sell.fulfillment.models.model_property import ModelProperty
from ebay_sell.fulfillment.models.name_value_pair import NameValuePair
from ebay_sell.fulfillment.models.tax import Tax
from ebay_sell._runtime import ApiModel


class LineItem(ApiModel):
    """LineItem model."""

    applied_promotions: Optional[List[AppliedPromotion]] = Field(default=None, alias="appliedPromotions")
    compatibility_properties: Optional[List[ModelProperty]] = Field(default=None, alias="compatibilityProperties")
    delivery_cost: Optional[DeliveryCost] = Field(default=None, alias="deliveryCost")
    discounted_line_item_cost: Optional[Amount] = Field(default=None, alias="discountedLineItemCost")
    ebay_collect_and_remit_taxes: Optional[List[EbayCollectAndRemitTax]] = Field(
        default=None, alias="ebayCollectAndRemitTaxes"
    )
    ebay_collected_charges: Optional[EbayCollectedCharges] = Field(default=None, alias="ebayCollectedCharges")
    gift_details: Optional[GiftDetails] = Field(default=None, alias="giftDetails")
    item_location: Optional[ItemLocation] = Field(default=None, alias="itemLocation")
    legacy_item_id: Optional[StrictStr] = Field(default=None, alias="legacyItemId")
    legacy_variation_id: Optional[StrictStr] = Field(default=None, alias="legacyVariationId")
    line_item_cost: Optional[Amount] = Field(default=None, alias="lineItemCost")
    line_item_fulfillment_instructions: Optional[LineItemFulfillmentInstructions] = Field(
        default=None, alias="lineItemFulfillmentInstructions"
    )
    line_item_fulfillment_status: Optional[StrictStr] = Field(default=None, alias="lineItemFulfillmentStatus")
    line_item_id: Optional[StrictStr] = Field(default=None, alias="lineItemId")
    linked_order_line_items: Optional[List[LinkedOrderLineItem]] = Field(default=None, alias="linkedOrderLineItems")
    listing_marketplace_id: Optional[StrictStr] = Field(default=None, alias="listingMarketplaceId")
    properties: Optional[LineItemProperties] = None
    purchase_marketplace_id: Optional[StrictStr] = Field(default=None, alias="purchaseMarketplaceId")
    quantity: Optional[StrictInt] = None
    refunds: Optional[List[LineItemRefund]] = None
    sku: Optional[StrictStr] = None
    sold_format: Optional[StrictStr] = Field(default=None, alias="soldFormat")
    taxes: Optional[List[Tax]] = None
    title: Optional[StrictStr] = None
    total: Optional[Amount] = None
    variation_aspects: Optional[List[NameValuePair]] = Field(default=None, alias="variationAspects")
