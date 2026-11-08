# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.disabled_product_filter import DisabledProductFilter
from ebay_sell.metadata.models.pagination_input import PaginationInput
from ebay_sell.metadata.models.product_identifier import ProductIdentifier
from ebay_sell.metadata.models.property_filter_inner import PropertyFilterInner
from ebay_sell.metadata.models.sort_order_inner import SortOrderInner
from ebay_sell._runtime import ApiModel


class ProductRequest(ApiModel):
    """ProductRequest model."""

    application_property_filters: Optional[List[PropertyFilterInner]] = Field(
        default=None, alias="applicationPropertyFilters"
    )
    dataset: Optional[List[StrictStr]] = None
    dataset_property_name: Optional[List[StrictStr]] = Field(default=None, alias="datasetPropertyName")
    disabled_product_filter: Optional[DisabledProductFilter] = Field(default=None, alias="disabledProductFilter")
    pagination_input: Optional[PaginationInput] = Field(default=None, alias="paginationInput")
    product_identifier: Optional[ProductIdentifier] = Field(default=None, alias="productIdentifier")
    sort_orders: Optional[List[SortOrderInner]] = Field(default=None, alias="sortOrders")
