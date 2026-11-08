# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.metadata.models.sales_tax_jurisdictions import SalesTaxJurisdictions

_get_sales_tax_jurisdictions: Operation[SalesTaxJurisdictions] = Operation(
    id="getSalesTaxJurisdictions",
    method="GET",
    path="/sell/metadata/v1/country/{countryCode}/sales_tax_jurisdiction",
    resource="countries",
    name="get_sales_tax_jurisdictions",
    params=(Param("countryCode", "country_code", "path"),),
    response=SalesTaxJurisdictions,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (_get_sales_tax_jurisdictions,)


class CountriesApi(Resource):
    @checked
    def get_sales_tax_jurisdictions(
        self,
        country_code: StrictStr,
    ) -> SalesTaxJurisdictions:
        """List the sales tax jurisdictions of a country."""
        return self._call(
            _get_sales_tax_jurisdictions,
            country_code=country_code,
        )


class AsyncCountriesApi(AsyncResource):
    @checked
    async def get_sales_tax_jurisdictions(
        self,
        country_code: StrictStr,
    ) -> SalesTaxJurisdictions:
        """List the sales tax jurisdictions of a country."""
        return await self._call(
            _get_sales_tax_jurisdictions,
            country_code=country_code,
        )
