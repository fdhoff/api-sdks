# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.ebay_fulfillment_program import EbayFulfillmentProgram
from ebay_sell.fulfillment.models.ebay_international_shipping import EbayInternationalShipping
from ebay_sell.fulfillment.models.ebay_shipping import EbayShipping
from ebay_sell.fulfillment.models.ebay_vault_program import EbayVaultProgram
from ebay_sell.fulfillment.models.post_sale_authentication_program import PostSaleAuthenticationProgram
from ebay_sell._runtime import ApiModel


class Program(ApiModel):
    """Program model."""

    authenticity_verification: Optional[PostSaleAuthenticationProgram] = Field(
        default=None, alias="authenticityVerification"
    )
    ebay_shipping: Optional[EbayShipping] = Field(default=None, alias="ebayShipping")
    ebay_vault: Optional[EbayVaultProgram] = Field(default=None, alias="ebayVault")
    ebay_international_shipping: Optional[EbayInternationalShipping] = Field(
        default=None, alias="ebayInternationalShipping"
    )
    fulfillment_program: Optional[EbayFulfillmentProgram] = Field(default=None, alias="fulfillmentProgram")
