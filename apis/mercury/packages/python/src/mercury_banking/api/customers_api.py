# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.api_v1_ar_customer_create_request import ApiV1ArCustomerCreateRequest
from mercury_banking.models.api_v1_ar_customer_paginated_response_data import ApiV1ArCustomerPaginatedResponseData
from mercury_banking.models.api_v1_ar_customer_response_data import ApiV1ArCustomerResponseData
from mercury_banking.models.api_v1_ar_customer_update_request import ApiV1ArCustomerUpdateRequest

_create_customer: Operation[ApiV1ArCustomerResponseData] = Operation(
    id="createCustomer",
    method="POST",
    path="/ar/customers",
    resource="customers",
    name="create",
    params=(),
    response=ApiV1ArCustomerResponseData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_delete_customer: Operation[None] = Operation(
    id="deleteCustomer",
    method="DELETE",
    path="/ar/customers/{customerId}",
    resource="customers",
    name="delete",
    params=(Param("customerId", "customer_id", "path"),),
    response=None,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_customer: Operation[ApiV1ArCustomerResponseData] = Operation(
    id="getCustomer",
    method="GET",
    path="/ar/customers/{customerId}",
    resource="customers",
    name="get",
    params=(Param("customerId", "customer_id", "path"),),
    response=ApiV1ArCustomerResponseData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_customers: Operation[ApiV1ArCustomerPaginatedResponseData] = Operation(
    id="listCustomers",
    method="GET",
    path="/ar/customers",
    resource="customers",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=ApiV1ArCustomerPaginatedResponseData,
    returns_json=True,
    iterator="iter",
    item=_models.ApiV1ArCustomerResponseData,
    paging=Cursor(items="customers", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_update_customer: Operation[ApiV1ArCustomerResponseData] = Operation(
    id="updateCustomer",
    method="POST",
    path="/ar/customers/{customerId}",
    resource="customers",
    name="update",
    params=(Param("customerId", "customer_id", "path"),),
    response=ApiV1ArCustomerResponseData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _create_customer,
    _delete_customer,
    _get_customer,
    _list_customers,
    _update_customer,
)


class CustomersApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[ApiV1ArCustomerCreateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArCustomerResponseData:
        """Create an invoicing customer."""
        return self._call(
            _create_customer,
            _body=body,
        )

    @checked
    def delete(
        self,
        customer_id: UUID,
    ) -> None:
        """Delete an invoicing customer."""
        return self._call(
            _delete_customer,
            customer_id=customer_id,
        )

    @checked
    def get(
        self,
        customer_id: UUID,
    ) -> ApiV1ArCustomerResponseData:
        """Get one invoicing customer."""
        return self._call(
            _get_customer,
            customer_id=customer_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1ArCustomerPaginatedResponseData:
        """List one page of invoicing customers."""
        return self._call(
            _list_customers,
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
    ) -> Iterator[_models.ApiV1ArCustomerResponseData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_customers,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def update(
        self,
        customer_id: UUID,
        body: Optional[Union[ApiV1ArCustomerUpdateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArCustomerResponseData:
        """Update an invoicing customer."""
        return self._call(
            _update_customer,
            customer_id=customer_id,
            _body=body,
        )


class AsyncCustomersApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[ApiV1ArCustomerCreateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArCustomerResponseData:
        """Create an invoicing customer."""
        return await self._call(
            _create_customer,
            _body=body,
        )

    @checked
    async def delete(
        self,
        customer_id: UUID,
    ) -> None:
        """Delete an invoicing customer."""
        return await self._call(
            _delete_customer,
            customer_id=customer_id,
        )

    @checked
    async def get(
        self,
        customer_id: UUID,
    ) -> ApiV1ArCustomerResponseData:
        """Get one invoicing customer."""
        return await self._call(
            _get_customer,
            customer_id=customer_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1ArCustomerPaginatedResponseData:
        """List one page of invoicing customers."""
        return await self._call(
            _list_customers,
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
    ) -> AsyncIterator[_models.ApiV1ArCustomerResponseData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_customers,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def update(
        self,
        customer_id: UUID,
        body: Optional[Union[ApiV1ArCustomerUpdateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArCustomerResponseData:
        """Update an invoicing customer."""
        return await self._call(
            _update_customer,
            customer_id=customer_id,
            _body=body,
        )
