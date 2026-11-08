# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_section import ShopSection
from etsy_seller.models.shop_sections import ShopSections

_create_shop_section: Operation[ShopSection] = Operation(
    id="createShopSection",
    method="POST",
    path="/v3/application/shops/{shop_id}/sections",
    resource="shop_sections",
    name="create",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("title", "title", "urlencoded"),
    ),
    response=ShopSection,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_delete_shop_section: Operation[None] = Operation(
    id="deleteShopSection",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/sections/{shop_section_id}",
    resource="shop_sections",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shop_section_id", "shop_section_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_get_shop_section: Operation[ShopSection] = Operation(
    id="getShopSection",
    method="GET",
    path="/v3/application/shops/{shop_id}/sections/{shop_section_id}",
    resource="shop_sections",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shop_section_id", "shop_section_id", "path"),
    ),
    response=ShopSection,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_shop_sections: Operation[ShopSections] = Operation(
    id="getShopSections",
    method="GET",
    path="/v3/application/shops/{shop_id}/sections",
    resource="shop_sections",
    name="list",
    params=(Param("shop_id", "shop_id", "path"),),
    response=ShopSections,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_update_shop_section: Operation[ShopSection] = Operation(
    id="updateShopSection",
    method="PUT",
    path="/v3/application/shops/{shop_id}/sections/{shop_section_id}",
    resource="shop_sections",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("shop_section_id", "shop_section_id", "path"),
        Param("title", "title", "urlencoded"),
    ),
    response=ShopSection,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)

OPERATIONS = (
    _create_shop_section,
    _delete_shop_section,
    _get_shop_section,
    _get_shop_sections,
    _update_shop_section,
)


class ShopSectionsApi(Resource):
    @checked
    def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: StrictStr,
    ) -> ShopSection:
        """Create a shop section."""
        return self._call(
            _create_shop_section,
            shop_id=shop_id,
            title=title,
        )

    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shop_section_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shop section."""
        return self._call(
            _delete_shop_section,
            shop_id=shop_id,
            shop_section_id=shop_section_id,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shop_section_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopSection:
        """Get one shop section."""
        return self._call(
            _get_shop_section,
            shop_id=shop_id,
            shop_section_id=shop_section_id,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopSections:
        """List a shop&#39;s sections."""
        return self._call(
            _get_shop_sections,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shop_section_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: StrictStr,
    ) -> ShopSection:
        """Rename a shop section."""
        return self._call(
            _update_shop_section,
            shop_id=shop_id,
            shop_section_id=shop_section_id,
            title=title,
        )


class AsyncShopSectionsApi(AsyncResource):
    @checked
    async def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: StrictStr,
    ) -> ShopSection:
        """Create a shop section."""
        return await self._call(
            _create_shop_section,
            shop_id=shop_id,
            title=title,
        )

    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shop_section_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a shop section."""
        return await self._call(
            _delete_shop_section,
            shop_id=shop_id,
            shop_section_id=shop_section_id,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shop_section_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopSection:
        """Get one shop section."""
        return await self._call(
            _get_shop_section,
            shop_id=shop_id,
            shop_section_id=shop_section_id,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopSections:
        """List a shop&#39;s sections."""
        return await self._call(
            _get_shop_sections,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        shop_section_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        title: StrictStr,
    ) -> ShopSection:
        """Rename a shop section."""
        return await self._call(
            _update_shop_section,
            shop_id=shop_id,
            shop_section_id=shop_section_id,
            title=title,
        )
