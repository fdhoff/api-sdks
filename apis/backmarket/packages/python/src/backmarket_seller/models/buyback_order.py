# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.buyback_order_customer import BuybackOrderCustomer
from backmarket_seller.models.buyback_order_listing import BuybackOrderListing
from backmarket_seller.models.buyback_order_original_price import BuybackOrderOriginalPrice
from backmarket_seller.models.buyback_order_return_address import BuybackOrderReturnAddress
from backmarket_seller.models.buyback_order_state import BuybackOrderState
from backmarket_seller.models.buyback_reason import BuybackReason
from backmarket_seller._runtime import ApiModel


class BuybackOrder(ApiModel):
    """BuybackOrder model."""

    order_public_id: StrictStr = Field(alias="orderPublicId")
    creation_date: StrictStr = Field(alias="creationDate")
    modification_date: StrictStr = Field(alias="modificationDate")
    shipping_date: StrictStr = Field(alias="shippingDate")
    suspension_date: Optional[StrictStr] = Field(default=None, alias="suspensionDate")
    receival_date: Optional[StrictStr] = Field(default=None, alias="receivalDate")
    payment_date: Optional[StrictStr] = Field(default=None, alias="paymentDate")
    counter_proposal_date: Optional[StrictStr] = Field(default=None, alias="counterProposalDate")
    status: BuybackOrderState
    market: StrictStr
    transfer_certificate_link: StrictStr = Field(alias="transferCertificateLink")
    listing: BuybackOrderListing
    customer: BuybackOrderCustomer
    return_address: BuybackOrderReturnAddress = Field(alias="returnAddress")
    original_price: BuybackOrderOriginalPrice = Field(alias="originalPrice")
    counter_offer_price: Optional[BuybackOrderOriginalPrice] = Field(default=None, alias="counterOfferPrice")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
    shipper: Optional[StrictStr] = None
    suspend_reasons: Optional[List[BuybackReason]] = Field(default=None, alias="suspendReasons")
    counter_offer_reasons: Optional[List[BuybackReason]] = Field(default=None, alias="counterOfferReasons")
