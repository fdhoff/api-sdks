# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_ar_product_paginated_response_data_page import (
    ApiV1ArProductPaginatedResponseDataPage,
)
from mercury_banking.models.api_v1_ar_product_response_data import ApiV1ArProductResponseData
from mercury_banking._runtime import ApiModel


class ApiV1ArProductPaginatedResponseData(ApiModel):
    """ApiV1ArProductPaginatedResponseData model."""

    page: ApiV1ArProductPaginatedResponseDataPage
    products: List[ApiV1ArProductResponseData]
