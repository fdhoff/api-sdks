# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.metadata.models.multi_compatibility_property_values_request import (
    MultiCompatibilityPropertyValuesRequest,
)
from ebay_sell.metadata.models.multi_compatibility_property_values_response import (
    MultiCompatibilityPropertyValuesResponse,
)
from ebay_sell.metadata.models.product_request import ProductRequest
from ebay_sell.metadata.models.product_response import ProductResponse
from ebay_sell.metadata.models.property_names_request import PropertyNamesRequest
from ebay_sell.metadata.models.property_names_response import PropertyNamesResponse
from ebay_sell.metadata.models.property_values_request import PropertyValuesRequest
from ebay_sell.metadata.models.property_values_response import PropertyValuesResponse
from ebay_sell.metadata.models.specification_request import SpecificationRequest
from ebay_sell.metadata.models.specification_response import SpecificationResponse

_get_compatibilities_by_specification: Operation[SpecificationResponse] = Operation(
    id="getCompatibilitiesBySpecification",
    method="POST",
    path="/sell/metadata/v1/compatibilities/get_compatibilities_by_specification",
    resource="compatibilities",
    name="get_by_specification",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=SpecificationResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_compatibility_property_names: Operation[PropertyNamesResponse] = Operation(
    id="getCompatibilityPropertyNames",
    method="POST",
    path="/sell/metadata/v1/compatibilities/get_compatibility_property_names",
    resource="compatibilities",
    name="get_property_names",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=PropertyNamesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_compatibility_property_values: Operation[PropertyValuesResponse] = Operation(
    id="getCompatibilityPropertyValues",
    method="POST",
    path="/sell/metadata/v1/compatibilities/get_compatibility_property_values",
    resource="compatibilities",
    name="get_property_values",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=PropertyValuesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_multi_compatibility_property_values: Operation[MultiCompatibilityPropertyValuesResponse] = Operation(
    id="getMultiCompatibilityPropertyValues",
    method="POST",
    path="/sell/metadata/v1/compatibilities/get_multi_compatibility_property_values",
    resource="compatibilities",
    name="get_multi_property_values",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=MultiCompatibilityPropertyValuesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_product_compatibilities: Operation[ProductResponse] = Operation(
    id="getProductCompatibilities",
    method="POST",
    path="/sell/metadata/v1/compatibilities/get_product_compatibilities",
    resource="compatibilities",
    name="get_product_compatibilities",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=ProductResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (
    _get_compatibilities_by_specification,
    _get_compatibility_property_names,
    _get_compatibility_property_values,
    _get_multi_compatibility_property_values,
    _get_product_compatibilities,
)


class CompatibilitiesApi(Resource):
    @checked
    def get_by_specification(
        self,
        body: Optional[Union[SpecificationRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SpecificationResponse:
        """List the vehicles that match a parts specification."""
        return self._call(
            _get_compatibilities_by_specification,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get_property_names(
        self,
        body: Optional[Union[PropertyNamesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PropertyNamesResponse:
        """List the compatibility property names of a category."""
        return self._call(
            _get_compatibility_property_names,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get_property_values(
        self,
        body: Optional[Union[PropertyValuesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PropertyValuesResponse:
        """List the values of one compatibility property."""
        return self._call(
            _get_compatibility_property_values,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get_multi_property_values(
        self,
        body: Optional[Union[MultiCompatibilityPropertyValuesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> MultiCompatibilityPropertyValuesResponse:
        """List the values of several compatibility properties."""
        return self._call(
            _get_multi_compatibility_property_values,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get_product_compatibilities(
        self,
        body: Optional[Union[ProductRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> ProductResponse:
        """List the vehicles a product fits."""
        return self._call(
            _get_product_compatibilities,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncCompatibilitiesApi(AsyncResource):
    @checked
    async def get_by_specification(
        self,
        body: Optional[Union[SpecificationRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SpecificationResponse:
        """List the vehicles that match a parts specification."""
        return await self._call(
            _get_compatibilities_by_specification,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get_property_names(
        self,
        body: Optional[Union[PropertyNamesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PropertyNamesResponse:
        """List the compatibility property names of a category."""
        return await self._call(
            _get_compatibility_property_names,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get_property_values(
        self,
        body: Optional[Union[PropertyValuesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PropertyValuesResponse:
        """List the values of one compatibility property."""
        return await self._call(
            _get_compatibility_property_values,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get_multi_property_values(
        self,
        body: Optional[Union[MultiCompatibilityPropertyValuesRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> MultiCompatibilityPropertyValuesResponse:
        """List the values of several compatibility properties."""
        return await self._call(
            _get_multi_compatibility_property_values,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get_product_compatibilities(
        self,
        body: Optional[Union[ProductRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> ProductResponse:
        """List the vehicles a product fits."""
        return await self._call(
            _get_product_compatibilities,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
