# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.pagination_input import PaginationInput
from ebay_sell.metadata.models.property_filter_inner import PropertyFilterInner
from ebay_sell.metadata.models.sort_order_inner import SortOrderInner
from ebay_sell._runtime import ApiModel


class SpecificationRequest(ApiModel):
    """SpecificationRequest model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    compatibility_property_filters: Optional[List[PropertyFilterInner]] = Field(
        default=None, alias="compatibilityPropertyFilters"
    )
    dataset: Optional[StrictStr] = None
    dataset_property_name: Optional[List[StrictStr]] = Field(default=None, alias="datasetPropertyName")
    exact_match: Optional[StrictBool] = Field(default=None, alias="exactMatch")
    pagination_input: Optional[PaginationInput] = Field(default=None, alias="paginationInput")
    sort_orders: Optional[List[SortOrderInner]] = Field(default=None, alias="sortOrders")
    specifications: Optional[List[PropertyFilterInner]] = None
