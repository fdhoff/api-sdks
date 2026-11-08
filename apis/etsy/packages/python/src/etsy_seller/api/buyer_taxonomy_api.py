# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.buyer_taxonomy_node_properties import BuyerTaxonomyNodeProperties
from etsy_seller.models.buyer_taxonomy_nodes import BuyerTaxonomyNodes

_get_buyer_taxonomy_nodes: Operation[BuyerTaxonomyNodes] = Operation(
    id="getBuyerTaxonomyNodes",
    method="GET",
    path="/v3/application/buyer-taxonomy/nodes",
    resource="buyer_taxonomy",
    name="list_nodes",
    params=(),
    response=BuyerTaxonomyNodes,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_properties_by_buyer_taxonomy_id: Operation[BuyerTaxonomyNodeProperties] = Operation(
    id="getPropertiesByBuyerTaxonomyId",
    method="GET",
    path="/v3/application/buyer-taxonomy/nodes/{taxonomy_id}/properties",
    resource="buyer_taxonomy",
    name="list_properties",
    params=(Param("taxonomy_id", "taxonomy_id", "path"),),
    response=BuyerTaxonomyNodeProperties,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)

OPERATIONS = (
    _get_buyer_taxonomy_nodes,
    _get_properties_by_buyer_taxonomy_id,
)


class BuyerTaxonomyApi(Resource):
    @checked
    def list_nodes(
        self,
    ) -> BuyerTaxonomyNodes:
        """List the buyer taxonomy tree."""
        return self._call(
            _get_buyer_taxonomy_nodes,
        )

    @checked
    def list_properties(
        self,
        taxonomy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> BuyerTaxonomyNodeProperties:
        """List the properties of one buyer taxonomy node."""
        return self._call(
            _get_properties_by_buyer_taxonomy_id,
            taxonomy_id=taxonomy_id,
        )


class AsyncBuyerTaxonomyApi(AsyncResource):
    @checked
    async def list_nodes(
        self,
    ) -> BuyerTaxonomyNodes:
        """List the buyer taxonomy tree."""
        return await self._call(
            _get_buyer_taxonomy_nodes,
        )

    @checked
    async def list_properties(
        self,
        taxonomy_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> BuyerTaxonomyNodeProperties:
        """List the properties of one buyer taxonomy node."""
        return await self._call(
            _get_properties_by_buyer_taxonomy_id,
            taxonomy_id=taxonomy_id,
        )
