# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.best_offer import BestOffer
from ebay_sell.inventory.models.regional_product_compliance_policies import RegionalProductCompliancePolicies
from ebay_sell.inventory.models.regional_take_back_policies import RegionalTakeBackPolicies
from ebay_sell.inventory.models.shipping_cost_override import ShippingCostOverride
from ebay_sell._runtime import ApiModel


class ListingPolicies(ApiModel):
    """ListingPolicies model."""

    best_offer_terms: Optional[BestOffer] = Field(default=None, alias="bestOfferTerms")
    e_bay_plus_if_eligible: Optional[StrictBool] = Field(default=None, alias="eBayPlusIfEligible")
    fulfillment_policy_id: Optional[StrictStr] = Field(default=None, alias="fulfillmentPolicyId")
    payment_policy_id: Optional[StrictStr] = Field(default=None, alias="paymentPolicyId")
    product_compliance_policy_ids: Optional[List[StrictStr]] = Field(default=None, alias="productCompliancePolicyIds")
    regional_product_compliance_policies: Optional[RegionalProductCompliancePolicies] = Field(
        default=None, alias="regionalProductCompliancePolicies"
    )
    regional_take_back_policies: Optional[RegionalTakeBackPolicies] = Field(
        default=None, alias="regionalTakeBackPolicies"
    )
    return_policy_id: Optional[StrictStr] = Field(default=None, alias="returnPolicyId")
    shipping_cost_overrides: Optional[List[ShippingCostOverride]] = Field(default=None, alias="shippingCostOverrides")
    take_back_policy_id: Optional[StrictStr] = Field(default=None, alias="takeBackPolicyId")
