# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_ar_customer_paginated_response_data_page import (
    ApiV1ArCustomerPaginatedResponseDataPage,
)
from mercury_banking.models.api_v1_ar_customer_response_data import ApiV1ArCustomerResponseData
from mercury_banking._runtime import ApiModel


class ApiV1ArCustomerPaginatedResponseData(ApiModel):
    """ApiV1ArCustomerPaginatedResponseData model."""

    customers: List[ApiV1ArCustomerResponseData]
    page: ApiV1ArCustomerPaginatedResponseDataPage
