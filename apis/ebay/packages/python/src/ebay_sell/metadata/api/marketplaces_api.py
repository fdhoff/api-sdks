# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.metadata.models.automotive_parts_compatibility_policy_response import (
    AutomotivePartsCompatibilityPolicyResponse,
)
from ebay_sell.metadata.models.category_policy_response import CategoryPolicyResponse
from ebay_sell.metadata.models.classified_ad_policy_response import ClassifiedAdPolicyResponse
from ebay_sell.metadata.models.extended_producer_responsibility_policy_response import (
    ExtendedProducerResponsibilityPolicyResponse,
)
from ebay_sell.metadata.models.get_currencies_response import GetCurrenciesResponse
from ebay_sell.metadata.models.hazardous_material_details_response import HazardousMaterialDetailsResponse
from ebay_sell.metadata.models.item_condition_policy_response import ItemConditionPolicyResponse
from ebay_sell.metadata.models.listing_structure_policy_response import ListingStructurePolicyResponse
from ebay_sell.metadata.models.listing_type_policies_response import ListingTypePoliciesResponse
from ebay_sell.metadata.models.motors_listing_policies_response import MotorsListingPoliciesResponse
from ebay_sell.metadata.models.negotiated_price_policy_response import NegotiatedPricePolicyResponse
from ebay_sell.metadata.models.product_safety_labels_response import ProductSafetyLabelsResponse
from ebay_sell.metadata.models.regulatory_policy_response import RegulatoryPolicyResponse
from ebay_sell.metadata.models.return_policy_response import ReturnPolicyResponse
from ebay_sell.metadata.models.shipping_policies_response import ShippingPoliciesResponse
from ebay_sell.metadata.models.site_visibility_policies_response import SiteVisibilityPoliciesResponse

_get_automotive_parts_compatibility_policies: Operation[AutomotivePartsCompatibilityPolicyResponse] = Operation(
    id="getAutomotivePartsCompatibilityPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies",
    resource="marketplaces",
    name="get_automotive_parts_compatibility_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=AutomotivePartsCompatibilityPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_category_policies: Operation[CategoryPolicyResponse] = Operation(
    id="getCategoryPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_category_policies",
    resource="marketplaces",
    name="get_category_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=CategoryPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_classified_ad_policies: Operation[ClassifiedAdPolicyResponse] = Operation(
    id="getClassifiedAdPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_classified_ad_policies",
    resource="marketplaces",
    name="get_classified_ad_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=ClassifiedAdPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_currencies: Operation[GetCurrenciesResponse] = Operation(
    id="getCurrencies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_currencies",
    resource="marketplaces",
    name="get_currencies",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=GetCurrenciesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_extended_producer_responsibility_policies: Operation[ExtendedProducerResponsibilityPolicyResponse] = Operation(
    id="getExtendedProducerResponsibilityPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_extended_producer_responsibility_policies",
    resource="marketplaces",
    name="get_extended_producer_responsibility_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=ExtendedProducerResponsibilityPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_hazardous_materials_labels: Operation[HazardousMaterialDetailsResponse] = Operation(
    id="getHazardousMaterialsLabels",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_hazardous_materials_labels",
    resource="marketplaces",
    name="get_hazardous_materials_labels",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=HazardousMaterialDetailsResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_item_condition_policies: Operation[ItemConditionPolicyResponse] = Operation(
    id="getItemConditionPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_item_condition_policies",
    resource="marketplaces",
    name="get_item_condition_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=ItemConditionPolicyResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                ),
            ),
        ),
    ),
    host="api",
)
_get_listing_structure_policies: Operation[ListingStructurePolicyResponse] = Operation(
    id="getListingStructurePolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_structure_policies",
    resource="marketplaces",
    name="get_listing_structure_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=ListingStructurePolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_listing_type_policies: Operation[ListingTypePoliciesResponse] = Operation(
    id="getListingTypePolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_type_policies",
    resource="marketplaces",
    name="get_listing_type_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=ListingTypePoliciesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_motors_listing_policies: Operation[MotorsListingPoliciesResponse] = Operation(
    id="getMotorsListingPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_motors_listing_policies",
    resource="marketplaces",
    name="get_motors_listing_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=MotorsListingPoliciesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_negotiated_price_policies: Operation[NegotiatedPricePolicyResponse] = Operation(
    id="getNegotiatedPricePolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_negotiated_price_policies",
    resource="marketplaces",
    name="get_negotiated_price_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=NegotiatedPricePolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_product_safety_labels: Operation[ProductSafetyLabelsResponse] = Operation(
    id="getProductSafetyLabels",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_product_safety_labels",
    resource="marketplaces",
    name="get_product_safety_labels",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=ProductSafetyLabelsResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_regulatory_policies: Operation[RegulatoryPolicyResponse] = Operation(
    id="getRegulatoryPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_regulatory_policies",
    resource="marketplaces",
    name="get_regulatory_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=RegulatoryPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_return_policies: Operation[ReturnPolicyResponse] = Operation(
    id="getReturnPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_return_policies",
    resource="marketplaces",
    name="get_return_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=ReturnPolicyResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_shipping_policies: Operation[ShippingPoliciesResponse] = Operation(
    id="getShippingPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_shipping_policies",
    resource="marketplaces",
    name="get_shipping_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=ShippingPoliciesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_site_visibility_policies: Operation[SiteVisibilityPoliciesResponse] = Operation(
    id="getSiteVisibilityPolicies",
    method="GET",
    path="/sell/metadata/v1/marketplace/{marketplace_id}/get_site_visibility_policies",
    resource="marketplaces",
    name="get_site_visibility_policies",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("filter", "filter", "query"),
    ),
    response=SiteVisibilityPoliciesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (
    _get_automotive_parts_compatibility_policies,
    _get_category_policies,
    _get_classified_ad_policies,
    _get_currencies,
    _get_extended_producer_responsibility_policies,
    _get_hazardous_materials_labels,
    _get_item_condition_policies,
    _get_listing_structure_policies,
    _get_listing_type_policies,
    _get_motors_listing_policies,
    _get_negotiated_price_policies,
    _get_product_safety_labels,
    _get_regulatory_policies,
    _get_return_policies,
    _get_shipping_policies,
    _get_site_visibility_policies,
)


class MarketplacesApi(Resource):
    @checked
    def get_automotive_parts_compatibility_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> AutomotivePartsCompatibilityPolicyResponse:
        """List the categories of a marketplace that support parts compatibility."""
        return self._call(
            _get_automotive_parts_compatibility_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_category_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> CategoryPolicyResponse:
        """List the listing policies of a marketplace's categories."""
        return self._call(
            _get_category_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_classified_ad_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ClassifiedAdPolicyResponse:
        """List the classified ad policies of a marketplace's categories."""
        return self._call(
            _get_classified_ad_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_currencies(
        self,
        marketplace_id: StrictStr,
    ) -> GetCurrenciesResponse:
        """Get the default currency of a marketplace."""
        return self._call(
            _get_currencies,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_extended_producer_responsibility_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ExtendedProducerResponsibilityPolicyResponse:
        """List the extended producer responsibility policies of a marketplace's categories."""
        return self._call(
            _get_extended_producer_responsibility_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_hazardous_materials_labels(
        self,
        marketplace_id: StrictStr,
    ) -> HazardousMaterialDetailsResponse:
        """List the hazardous materials labels a marketplace accepts."""
        return self._call(
            _get_hazardous_materials_labels,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_item_condition_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ItemConditionPolicyResponse:
        """List the item conditions a marketplace's categories accept."""
        return self._call(
            _get_item_condition_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_listing_structure_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ListingStructurePolicyResponse:
        """List which of a marketplace's categories accept multi-variation listings."""
        return self._call(
            _get_listing_structure_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_listing_type_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ListingTypePoliciesResponse:
        """List the listing formats and durations of a marketplace's categories."""
        return self._call(
            _get_listing_type_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_motors_listing_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> MotorsListingPoliciesResponse:
        """List the motors listing policies of a marketplace's categories."""
        return self._call(
            _get_motors_listing_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_negotiated_price_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> NegotiatedPricePolicyResponse:
        """List the Best Offer policies of a marketplace's categories."""
        return self._call(
            _get_negotiated_price_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_product_safety_labels(
        self,
        marketplace_id: StrictStr,
    ) -> ProductSafetyLabelsResponse:
        """List the product safety labels a marketplace accepts."""
        return self._call(
            _get_product_safety_labels,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_regulatory_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> RegulatoryPolicyResponse:
        """List the regulatory policies of a marketplace's categories."""
        return self._call(
            _get_regulatory_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_return_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ReturnPolicyResponse:
        """List the return policies of a marketplace's categories."""
        return self._call(
            _get_return_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_shipping_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ShippingPoliciesResponse:
        """List the shipping policies of a marketplace's categories."""
        return self._call(
            _get_shipping_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    def get_site_visibility_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> SiteVisibilityPoliciesResponse:
        """List which of a marketplace's categories show on other marketplaces."""
        return self._call(
            _get_site_visibility_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )


class AsyncMarketplacesApi(AsyncResource):
    @checked
    async def get_automotive_parts_compatibility_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> AutomotivePartsCompatibilityPolicyResponse:
        """List the categories of a marketplace that support parts compatibility."""
        return await self._call(
            _get_automotive_parts_compatibility_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_category_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> CategoryPolicyResponse:
        """List the listing policies of a marketplace's categories."""
        return await self._call(
            _get_category_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_classified_ad_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ClassifiedAdPolicyResponse:
        """List the classified ad policies of a marketplace's categories."""
        return await self._call(
            _get_classified_ad_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_currencies(
        self,
        marketplace_id: StrictStr,
    ) -> GetCurrenciesResponse:
        """Get the default currency of a marketplace."""
        return await self._call(
            _get_currencies,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_extended_producer_responsibility_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ExtendedProducerResponsibilityPolicyResponse:
        """List the extended producer responsibility policies of a marketplace's categories."""
        return await self._call(
            _get_extended_producer_responsibility_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_hazardous_materials_labels(
        self,
        marketplace_id: StrictStr,
    ) -> HazardousMaterialDetailsResponse:
        """List the hazardous materials labels a marketplace accepts."""
        return await self._call(
            _get_hazardous_materials_labels,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_item_condition_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ItemConditionPolicyResponse:
        """List the item conditions a marketplace's categories accept."""
        return await self._call(
            _get_item_condition_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_listing_structure_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ListingStructurePolicyResponse:
        """List which of a marketplace's categories accept multi-variation listings."""
        return await self._call(
            _get_listing_structure_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_listing_type_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ListingTypePoliciesResponse:
        """List the listing formats and durations of a marketplace's categories."""
        return await self._call(
            _get_listing_type_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_motors_listing_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> MotorsListingPoliciesResponse:
        """List the motors listing policies of a marketplace's categories."""
        return await self._call(
            _get_motors_listing_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_negotiated_price_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> NegotiatedPricePolicyResponse:
        """List the Best Offer policies of a marketplace's categories."""
        return await self._call(
            _get_negotiated_price_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_product_safety_labels(
        self,
        marketplace_id: StrictStr,
    ) -> ProductSafetyLabelsResponse:
        """List the product safety labels a marketplace accepts."""
        return await self._call(
            _get_product_safety_labels,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_regulatory_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> RegulatoryPolicyResponse:
        """List the regulatory policies of a marketplace's categories."""
        return await self._call(
            _get_regulatory_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_return_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ReturnPolicyResponse:
        """List the return policies of a marketplace's categories."""
        return await self._call(
            _get_return_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_shipping_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> ShippingPoliciesResponse:
        """List the shipping policies of a marketplace's categories."""
        return await self._call(
            _get_shipping_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )

    @checked
    async def get_site_visibility_policies(
        self,
        marketplace_id: StrictStr,
        *,
        filter: Optional[StrictStr] = None,
    ) -> SiteVisibilityPoliciesResponse:
        """List which of a marketplace's categories show on other marketplaces."""
        return await self._call(
            _get_site_visibility_policies,
            marketplace_id=marketplace_id,
            filter=filter,
        )
