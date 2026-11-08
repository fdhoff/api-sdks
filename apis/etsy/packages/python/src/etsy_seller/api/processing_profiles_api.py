# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_processing_profile import ShopProcessingProfile
from etsy_seller.models.shop_processing_profiles import ShopProcessingProfiles

_create_shop_readiness_state_definition: Operation[ShopProcessingProfile] = Operation(
    id="createShopReadinessStateDefinition",
    method="POST",
    path="/v3/application/shops/{shop_id}/readiness-state-definitions",
    resource="processing_profiles",
    name="create",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("readiness_state", "readiness_state", "urlencoded"),
        Param("min_processing_time", "min_processing_time", "urlencoded"),
        Param("max_processing_time", "max_processing_time", "urlencoded"),
        Param("processing_time_unit", "processing_time_unit", "urlencoded"),
    ),
    response=ShopProcessingProfile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_delete_shop_readiness_state_definition: Operation[None] = Operation(
    id="deleteShopReadinessStateDefinition",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}",
    resource="processing_profiles",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("readiness_state_definition_id", "readiness_state_definition_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)
_get_shop_readiness_state_definition: Operation[ShopProcessingProfile] = Operation(
    id="getShopReadinessStateDefinition",
    method="GET",
    path="/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}",
    resource="processing_profiles",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("readiness_state_definition_id", "readiness_state_definition_id", "path"),
    ),
    response=ShopProcessingProfile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_get_shop_readiness_state_definitions: Operation[ShopProcessingProfiles] = Operation(
    id="getShopReadinessStateDefinitions",
    method="GET",
    path="/v3/application/shops/{shop_id}/readiness-state-definitions",
    resource="processing_profiles",
    name="list",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=ShopProcessingProfiles,
    returns_json=True,
    iterator="iter",
    item=_models.ShopProcessingProfile,
    paging=Offset(items="results", total="count", offset="offset"),
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_update_shop_readiness_state_definition: Operation[ShopProcessingProfile] = Operation(
    id="updateShopReadinessStateDefinition",
    method="PUT",
    path="/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}",
    resource="processing_profiles",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("readiness_state_definition_id", "readiness_state_definition_id", "path"),
        Param("readiness_state", "readiness_state", "urlencoded"),
        Param("min_processing_time", "min_processing_time", "urlencoded"),
        Param("max_processing_time", "max_processing_time", "urlencoded"),
        Param("processing_time_unit", "processing_time_unit", "urlencoded"),
    ),
    response=ShopProcessingProfile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_w",)),
        ),
    ),
)

OPERATIONS = (
    _create_shop_readiness_state_definition,
    _delete_shop_readiness_state_definition,
    _get_shop_readiness_state_definition,
    _get_shop_readiness_state_definitions,
    _update_shop_readiness_state_definition,
)


class ProcessingProfilesApi(Resource):
    @checked
    def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        readiness_state: StrictStr,
        min_processing_time: Annotated[int, Field(le=10, strict=True, ge=1)],
        max_processing_time: Annotated[int, Field(le=10, strict=True, ge=1)],
        processing_time_unit: Optional[StrictStr] = None,
    ) -> ShopProcessingProfile:
        """Create a processing profile."""
        return self._call(
            _create_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state=readiness_state,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
        )

    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        readiness_state_definition_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a processing profile."""
        return self._call(
            _delete_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state_definition_id=readiness_state_definition_id,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        readiness_state_definition_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopProcessingProfile:
        """Get one processing profile."""
        return self._call(
            _get_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state_definition_id=readiness_state_definition_id,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> ShopProcessingProfiles:
        """List one page of a shop&#39;s processing profiles."""
        return self._call(
            _get_shop_readiness_state_definitions,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.ShopProcessingProfile]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_readiness_state_definitions,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        readiness_state_definition_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        readiness_state: Optional[StrictStr] = None,
        min_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        max_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        processing_time_unit: Optional[StrictStr] = None,
    ) -> ShopProcessingProfile:
        """Update a processing profile."""
        return self._call(
            _update_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state_definition_id=readiness_state_definition_id,
            readiness_state=readiness_state,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
        )


class AsyncProcessingProfilesApi(AsyncResource):
    @checked
    async def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        readiness_state: StrictStr,
        min_processing_time: Annotated[int, Field(le=10, strict=True, ge=1)],
        max_processing_time: Annotated[int, Field(le=10, strict=True, ge=1)],
        processing_time_unit: Optional[StrictStr] = None,
    ) -> ShopProcessingProfile:
        """Create a processing profile."""
        return await self._call(
            _create_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state=readiness_state,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
        )

    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        readiness_state_definition_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a processing profile."""
        return await self._call(
            _delete_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state_definition_id=readiness_state_definition_id,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        readiness_state_definition_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopProcessingProfile:
        """Get one processing profile."""
        return await self._call(
            _get_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state_definition_id=readiness_state_definition_id,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> ShopProcessingProfiles:
        """List one page of a shop&#39;s processing profiles."""
        return await self._call(
            _get_shop_readiness_state_definitions,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.ShopProcessingProfile]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_shop_readiness_state_definitions,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        readiness_state_definition_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        readiness_state: Optional[StrictStr] = None,
        min_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        max_processing_time: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = None,
        processing_time_unit: Optional[StrictStr] = None,
    ) -> ShopProcessingProfile:
        """Update a processing profile."""
        return await self._call(
            _update_shop_readiness_state_definition,
            shop_id=shop_id,
            readiness_state_definition_id=readiness_state_definition_id,
            readiness_state=readiness_state,
            min_processing_time=min_processing_time,
            max_processing_time=max_processing_time,
            processing_time_unit=processing_time_unit,
        )
