# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.bulk_sales_tax_input import BulkSalesTaxInput
from ebay_sell.account.models.sales_tax import SalesTax
from ebay_sell.account.models.sales_tax_base import SalesTaxBase
from ebay_sell.account.models.sales_taxes import SalesTaxes
from ebay_sell.account.models.updated_sales_tax_response import UpdatedSalesTaxResponse

_bulk_create_or_replace_sales_tax: Operation[UpdatedSalesTaxResponse] = Operation(
    id="bulkCreateOrReplaceSalesTax",
    method="POST",
    path="/sell/account/v1/bulk_create_or_replace_sales_tax",
    resource="sales_taxes",
    name="bulk_create_or_replace",
    params=(),
    response=UpdatedSalesTaxResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_create_or_replace_sales_tax: Operation[None] = Operation(
    id="createOrReplaceSalesTax",
    method="PUT",
    path="/sell/account/v1/sales_tax/{countryCode}/{jurisdictionId}",
    resource="sales_taxes",
    name="create_or_replace",
    params=(
        Param("countryCode", "country_code", "path"),
        Param("jurisdictionId", "jurisdiction_id", "path"),
    ),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_delete_sales_tax: Operation[None] = Operation(
    id="deleteSalesTax",
    method="DELETE",
    path="/sell/account/v1/sales_tax/{countryCode}/{jurisdictionId}",
    resource="sales_taxes",
    name="delete",
    params=(
        Param("countryCode", "country_code", "path"),
        Param("jurisdictionId", "jurisdiction_id", "path"),
    ),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_get_sales_tax: Operation[SalesTax] = Operation(
    id="getSalesTax",
    method="GET",
    path="/sell/account/v1/sales_tax/{countryCode}/{jurisdictionId}",
    resource="sales_taxes",
    name="get",
    params=(
        Param("countryCode", "country_code", "path"),
        Param("jurisdictionId", "jurisdiction_id", "path"),
    ),
    response=SalesTax,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.account",
                    "https://api.ebay.com/oauth/api_scope/sell.account.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_sales_taxes: Operation[SalesTaxes] = Operation(
    id="getSalesTaxes",
    method="GET",
    path="/sell/account/v1/sales_tax",
    resource="sales_taxes",
    name="list",
    params=(Param("country_code", "country_code", "query"),),
    response=SalesTaxes,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.account",
                    "https://api.ebay.com/oauth/api_scope/sell.account.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _bulk_create_or_replace_sales_tax,
    _create_or_replace_sales_tax,
    _delete_sales_tax,
    _get_sales_tax,
    _get_sales_taxes,
)


class SalesTaxesApi(Resource):
    @checked
    def bulk_create_or_replace(
        self,
        body: Union[BulkSalesTaxInput, Mapping[str, Any]],
    ) -> UpdatedSalesTaxResponse:
        """Set the seller's sales tax rates for several jurisdictions."""
        return self._call(
            _bulk_create_or_replace_sales_tax,
            _body=body,
        )

    @checked
    def create_or_replace(
        self,
        country_code: StrictStr,
        jurisdiction_id: StrictStr,
        body: Union[SalesTaxBase, Mapping[str, Any]],
    ) -> None:
        """Set the seller's sales tax rate for one jurisdiction."""
        return self._call(
            _create_or_replace_sales_tax,
            country_code=country_code,
            jurisdiction_id=jurisdiction_id,
            _body=body,
        )

    @checked
    def delete(
        self,
        country_code: StrictStr,
        jurisdiction_id: StrictStr,
    ) -> None:
        """Remove the seller's sales tax rate for one jurisdiction."""
        return self._call(
            _delete_sales_tax,
            country_code=country_code,
            jurisdiction_id=jurisdiction_id,
        )

    @checked
    def get(
        self,
        country_code: StrictStr,
        jurisdiction_id: StrictStr,
    ) -> SalesTax:
        """Get the seller's sales tax rate for one jurisdiction."""
        return self._call(
            _get_sales_tax,
            country_code=country_code,
            jurisdiction_id=jurisdiction_id,
        )

    @checked
    def list(
        self,
        *,
        country_code: StrictStr,
    ) -> SalesTaxes:
        """List the seller's sales tax rates for a country."""
        return self._call(
            _get_sales_taxes,
            country_code=country_code,
        )


class AsyncSalesTaxesApi(AsyncResource):
    @checked
    async def bulk_create_or_replace(
        self,
        body: Union[BulkSalesTaxInput, Mapping[str, Any]],
    ) -> UpdatedSalesTaxResponse:
        """Set the seller's sales tax rates for several jurisdictions."""
        return await self._call(
            _bulk_create_or_replace_sales_tax,
            _body=body,
        )

    @checked
    async def create_or_replace(
        self,
        country_code: StrictStr,
        jurisdiction_id: StrictStr,
        body: Union[SalesTaxBase, Mapping[str, Any]],
    ) -> None:
        """Set the seller's sales tax rate for one jurisdiction."""
        return await self._call(
            _create_or_replace_sales_tax,
            country_code=country_code,
            jurisdiction_id=jurisdiction_id,
            _body=body,
        )

    @checked
    async def delete(
        self,
        country_code: StrictStr,
        jurisdiction_id: StrictStr,
    ) -> None:
        """Remove the seller's sales tax rate for one jurisdiction."""
        return await self._call(
            _delete_sales_tax,
            country_code=country_code,
            jurisdiction_id=jurisdiction_id,
        )

    @checked
    async def get(
        self,
        country_code: StrictStr,
        jurisdiction_id: StrictStr,
    ) -> SalesTax:
        """Get the seller's sales tax rate for one jurisdiction."""
        return await self._call(
            _get_sales_tax,
            country_code=country_code,
            jurisdiction_id=jurisdiction_id,
        )

    @checked
    async def list(
        self,
        *,
        country_code: StrictStr,
    ) -> SalesTaxes:
        """List the seller's sales tax rates for a country."""
        return await self._call(
            _get_sales_taxes,
            country_code=country_code,
        )
