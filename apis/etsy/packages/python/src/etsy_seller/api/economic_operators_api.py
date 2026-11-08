# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_economic_operator import ShopEconomicOperator
from etsy_seller.models.shop_economic_operators import ShopEconomicOperators

_create_shop_economic_operator: Operation[ShopEconomicOperator] = Operation(
    id="createShopEconomicOperator",
    method="POST",
    path="/v3/application/shops/{shop_id}/economic-operators",
    resource="economic_operators",
    name="create",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("operator_name", "operator_name", "urlencoded"),
        Param("email", "email", "urlencoded"),
        Param("first_line", "first_line", "urlencoded"),
        Param("city", "city", "urlencoded"),
        Param("zip", "zip", "urlencoded"),
        Param("country_iso", "country_iso", "urlencoded"),
        Param("phone", "phone", "urlencoded"),
        Param("second_line", "second_line", "urlencoded"),
        Param("state", "state", "urlencoded"),
        Param("phone_country_iso", "phone_country_iso", "urlencoded"),
        Param("trademark_name", "trademark_name", "urlencoded"),
    ),
    response=ShopEconomicOperator,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_get_shop_economic_operator: Operation[ShopEconomicOperator] = Operation(
    id="getShopEconomicOperator",
    method="GET",
    path="/v3/application/shops/{shop_id}/economic-operators/{economic_operator_id}",
    resource="economic_operators",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("economic_operator_id", "economic_operator_id", "path"),
    ),
    response=ShopEconomicOperator,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_get_shop_economic_operators: Operation[ShopEconomicOperators] = Operation(
    id="getShopEconomicOperators",
    method="GET",
    path="/v3/application/shops/{shop_id}/economic-operators",
    resource="economic_operators",
    name="list",
    params=(Param("shop_id", "shop_id", "path"),),
    response=ShopEconomicOperators,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_update_shop_economic_operator: Operation[ShopEconomicOperator] = Operation(
    id="updateShopEconomicOperator",
    method="PATCH",
    path="/v3/application/shops/{shop_id}/economic-operators/{economic_operator_id}",
    resource="economic_operators",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("economic_operator_id", "economic_operator_id", "path"),
        Param("operator_name", "operator_name", "urlencoded"),
        Param("email", "email", "urlencoded"),
        Param("first_line", "first_line", "urlencoded"),
        Param("second_line", "second_line", "urlencoded"),
        Param("city", "city", "urlencoded"),
        Param("state", "state", "urlencoded"),
        Param("zip", "zip", "urlencoded"),
        Param("country_iso", "country_iso", "urlencoded"),
        Param("phone", "phone", "urlencoded"),
        Param("phone_country_iso", "phone_country_iso", "urlencoded"),
        Param("trademark_name", "trademark_name", "urlencoded"),
    ),
    response=ShopEconomicOperator,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _create_shop_economic_operator,
    _get_shop_economic_operator,
    _get_shop_economic_operators,
    _update_shop_economic_operator,
)


class EconomicOperatorsApi(Resource):
    @checked
    def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        operator_name: StrictStr,
        email: StrictStr,
        first_line: StrictStr,
        city: StrictStr,
        zip: StrictStr,
        country_iso: StrictStr,
        phone: StrictStr,
        second_line: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        phone_country_iso: Optional[StrictStr] = None,
        trademark_name: Optional[StrictStr] = None,
    ) -> ShopEconomicOperator:
        """Add an economic operator to a shop."""
        return self._call(
            _create_shop_economic_operator,
            shop_id=shop_id,
            operator_name=operator_name,
            email=email,
            first_line=first_line,
            city=city,
            zip=zip,
            country_iso=country_iso,
            phone=phone,
            second_line=second_line,
            state=state,
            phone_country_iso=phone_country_iso,
            trademark_name=trademark_name,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        economic_operator_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopEconomicOperator:
        """Get one economic operator."""
        return self._call(
            _get_shop_economic_operator,
            shop_id=shop_id,
            economic_operator_id=economic_operator_id,
        )

    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopEconomicOperators:
        """List a shop's economic operators."""
        return self._call(
            _get_shop_economic_operators,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        economic_operator_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        operator_name: Optional[StrictStr] = None,
        email: Optional[StrictStr] = None,
        first_line: Optional[StrictStr] = None,
        second_line: Optional[StrictStr] = None,
        city: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        zip: Optional[StrictStr] = None,
        country_iso: Optional[StrictStr] = None,
        phone: Optional[StrictStr] = None,
        phone_country_iso: Optional[StrictStr] = None,
        trademark_name: Optional[StrictStr] = None,
    ) -> ShopEconomicOperator:
        """Update an economic operator."""
        return self._call(
            _update_shop_economic_operator,
            shop_id=shop_id,
            economic_operator_id=economic_operator_id,
            operator_name=operator_name,
            email=email,
            first_line=first_line,
            second_line=second_line,
            city=city,
            state=state,
            zip=zip,
            country_iso=country_iso,
            phone=phone,
            phone_country_iso=phone_country_iso,
            trademark_name=trademark_name,
        )


class AsyncEconomicOperatorsApi(AsyncResource):
    @checked
    async def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        operator_name: StrictStr,
        email: StrictStr,
        first_line: StrictStr,
        city: StrictStr,
        zip: StrictStr,
        country_iso: StrictStr,
        phone: StrictStr,
        second_line: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        phone_country_iso: Optional[StrictStr] = None,
        trademark_name: Optional[StrictStr] = None,
    ) -> ShopEconomicOperator:
        """Add an economic operator to a shop."""
        return await self._call(
            _create_shop_economic_operator,
            shop_id=shop_id,
            operator_name=operator_name,
            email=email,
            first_line=first_line,
            city=city,
            zip=zip,
            country_iso=country_iso,
            phone=phone,
            second_line=second_line,
            state=state,
            phone_country_iso=phone_country_iso,
            trademark_name=trademark_name,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        economic_operator_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopEconomicOperator:
        """Get one economic operator."""
        return await self._call(
            _get_shop_economic_operator,
            shop_id=shop_id,
            economic_operator_id=economic_operator_id,
        )

    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopEconomicOperators:
        """List a shop's economic operators."""
        return await self._call(
            _get_shop_economic_operators,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        economic_operator_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        operator_name: Optional[StrictStr] = None,
        email: Optional[StrictStr] = None,
        first_line: Optional[StrictStr] = None,
        second_line: Optional[StrictStr] = None,
        city: Optional[StrictStr] = None,
        state: Optional[StrictStr] = None,
        zip: Optional[StrictStr] = None,
        country_iso: Optional[StrictStr] = None,
        phone: Optional[StrictStr] = None,
        phone_country_iso: Optional[StrictStr] = None,
        trademark_name: Optional[StrictStr] = None,
    ) -> ShopEconomicOperator:
        """Update an economic operator."""
        return await self._call(
            _update_shop_economic_operator,
            shop_id=shop_id,
            economic_operator_id=economic_operator_id,
            operator_name=operator_name,
            email=email,
            first_line=first_line,
            second_line=second_line,
            city=city,
            state=state,
            zip=zip,
            country_iso=country_iso,
            phone=phone,
            phone_country_iso=phone_country_iso,
            trademark_name=trademark_name,
        )
