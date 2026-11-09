# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing.models.item_price_markdown import ItemPriceMarkdown

_create_item_price_markdown_promotion: Operation[object] = Operation(
    id="createItemPriceMarkdownPromotion",
    method="POST",
    path="/sell/marketing/v1/item_price_markdown",
    resource="item_price_markdowns",
    name="create",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_delete_item_price_markdown_promotion: Operation[None] = Operation(
    id="deleteItemPriceMarkdownPromotion",
    method="DELETE",
    path="/sell/marketing/v1/item_price_markdown/{promotion_id}",
    resource="item_price_markdowns",
    name="delete",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_item_price_markdown_promotion: Operation[ItemPriceMarkdown] = Operation(
    id="getItemPriceMarkdownPromotion",
    method="GET",
    path="/sell/marketing/v1/item_price_markdown/{promotion_id}",
    resource="item_price_markdowns",
    name="get",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=ItemPriceMarkdown,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_update_item_price_markdown_promotion: Operation[object] = Operation(
    id="updateItemPriceMarkdownPromotion",
    method="PUT",
    path="/sell/marketing/v1/item_price_markdown/{promotion_id}",
    resource="item_price_markdowns",
    name="update",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _create_item_price_markdown_promotion,
    _delete_item_price_markdown_promotion,
    _get_item_price_markdown_promotion,
    _update_item_price_markdown_promotion,
)


class ItemPriceMarkdownsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[ItemPriceMarkdown, Mapping[str, Any]]] = None,
    ) -> object:
        """Create a markdown sale."""
        return self._call(
            _create_item_price_markdown_promotion,
            _body=body,
        )

    @checked
    def delete(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Delete a markdown sale."""
        return self._call(
            _delete_item_price_markdown_promotion,
            promotion_id=promotion_id,
        )

    @checked
    def get(
        self,
        promotion_id: StrictStr,
    ) -> ItemPriceMarkdown:
        """Get one markdown sale."""
        return self._call(
            _get_item_price_markdown_promotion,
            promotion_id=promotion_id,
        )

    @checked
    def update(
        self,
        promotion_id: StrictStr,
        body: Optional[Union[ItemPriceMarkdown, Mapping[str, Any]]] = None,
    ) -> object:
        """Replace a markdown sale."""
        return self._call(
            _update_item_price_markdown_promotion,
            promotion_id=promotion_id,
            _body=body,
        )


class AsyncItemPriceMarkdownsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[ItemPriceMarkdown, Mapping[str, Any]]] = None,
    ) -> object:
        """Create a markdown sale."""
        return await self._call(
            _create_item_price_markdown_promotion,
            _body=body,
        )

    @checked
    async def delete(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Delete a markdown sale."""
        return await self._call(
            _delete_item_price_markdown_promotion,
            promotion_id=promotion_id,
        )

    @checked
    async def get(
        self,
        promotion_id: StrictStr,
    ) -> ItemPriceMarkdown:
        """Get one markdown sale."""
        return await self._call(
            _get_item_price_markdown_promotion,
            promotion_id=promotion_id,
        )

    @checked
    async def update(
        self,
        promotion_id: StrictStr,
        body: Optional[Union[ItemPriceMarkdown, Mapping[str, Any]]] = None,
    ) -> object:
        """Replace a markdown sale."""
        return await self._call(
            _update_item_price_markdown_promotion,
            promotion_id=promotion_id,
            _body=body,
        )
