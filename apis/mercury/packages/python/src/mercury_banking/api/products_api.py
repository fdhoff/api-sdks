# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.api_v1_ar_product_create_request import ApiV1ArProductCreateRequest
from mercury_banking.models.api_v1_ar_product_paginated_response_data import ApiV1ArProductPaginatedResponseData
from mercury_banking.models.api_v1_ar_product_response_data import ApiV1ArProductResponseData

_create_product: Operation[ApiV1ArProductResponseData] = Operation(
    id="createProduct",
    method="POST",
    path="/ar/products",
    resource="products",
    name="create",
    params=(),
    response=ApiV1ArProductResponseData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_delete_product: Operation[None] = Operation(
    id="deleteProduct",
    method="DELETE",
    path="/ar/products/{productId}",
    resource="products",
    name="delete",
    params=(Param("productId", "product_id", "path"),),
    response=None,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_products: Operation[ApiV1ArProductPaginatedResponseData] = Operation(
    id="listProducts",
    method="GET",
    path="/ar/products",
    resource="products",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=ApiV1ArProductPaginatedResponseData,
    returns_json=True,
    iterator="iter",
    item=_models.ApiV1ArProductResponseData,
    paging=Cursor(items="products", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _create_product,
    _delete_product,
    _list_products,
)


class ProductsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[ApiV1ArProductCreateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArProductResponseData:
        """Create an invoicing product."""
        return self._call(
            _create_product,
            _body=body,
        )

    @checked
    def delete(
        self,
        product_id: UUID,
    ) -> None:
        """Delete an invoicing product."""
        return self._call(
            _delete_product,
            product_id=product_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1ArProductPaginatedResponseData:
        """List one page of invoicing products."""
        return self._call(
            _list_products,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ApiV1ArProductResponseData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_products,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )


class AsyncProductsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[ApiV1ArProductCreateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArProductResponseData:
        """Create an invoicing product."""
        return await self._call(
            _create_product,
            _body=body,
        )

    @checked
    async def delete(
        self,
        product_id: UUID,
    ) -> None:
        """Delete an invoicing product."""
        return await self._call(
            _delete_product,
            product_id=product_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1ArProductPaginatedResponseData:
        """List one page of invoicing products."""
        return await self._call(
            _list_products,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ApiV1ArProductResponseData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_products,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )
