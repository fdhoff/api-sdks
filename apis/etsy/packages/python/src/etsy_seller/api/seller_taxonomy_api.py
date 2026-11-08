# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import Field, StrictBool
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.seller_taxonomy_nodes import SellerTaxonomyNodes
from etsy_seller.models.taxonomy_node_properties import TaxonomyNodeProperties

_get_properties_by_taxonomy_id: Operation[TaxonomyNodeProperties] = Operation(
    id="getPropertiesByTaxonomyId",
    method="GET",
    path="/v3/application/seller-taxonomy/nodes/{taxonomy_id}/properties",
    resource="seller_taxonomy",
    name="list_properties",
    params=(
        Param("taxonomy_id", "taxonomy_id", "path"),
        Param("supports_variations", "supports_variations", "query"),
        Param("supports_attributes", "supports_attributes", "query"),
    ),
    response=TaxonomyNodeProperties,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_seller_taxonomy_nodes: Operation[SellerTaxonomyNodes] = Operation(
    id="getSellerTaxonomyNodes",
    method="GET",
    path="/v3/application/seller-taxonomy/nodes",
    resource="seller_taxonomy",
    name="list_nodes",
    params=(),
    response=SellerTaxonomyNodes,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)

OPERATIONS = (
    _get_properties_by_taxonomy_id,
    _get_seller_taxonomy_nodes,
)


class SellerTaxonomyApi(Resource):
    @checked
    def list_properties(
        self,
        taxonomy_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        supports_variations: Optional[StrictBool] = None,
        supports_attributes: Optional[StrictBool] = None,
    ) -> TaxonomyNodeProperties:
        """List the properties of one seller taxonomy node."""
        return self._call(
            _get_properties_by_taxonomy_id,
            taxonomy_id=taxonomy_id,
            supports_variations=supports_variations,
            supports_attributes=supports_attributes,
        )

    @checked
    def list_nodes(
        self,
    ) -> SellerTaxonomyNodes:
        """List the seller taxonomy tree."""
        return self._call(
            _get_seller_taxonomy_nodes,
        )


class AsyncSellerTaxonomyApi(AsyncResource):
    @checked
    async def list_properties(
        self,
        taxonomy_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        supports_variations: Optional[StrictBool] = None,
        supports_attributes: Optional[StrictBool] = None,
    ) -> TaxonomyNodeProperties:
        """List the properties of one seller taxonomy node."""
        return await self._call(
            _get_properties_by_taxonomy_id,
            taxonomy_id=taxonomy_id,
            supports_variations=supports_variations,
            supports_attributes=supports_attributes,
        )

    @checked
    async def list_nodes(
        self,
    ) -> SellerTaxonomyNodes:
        """List the seller taxonomy tree."""
        return await self._call(
            _get_seller_taxonomy_nodes,
        )
