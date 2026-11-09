# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.merchant_info import MerchantInfo
from mercury_banking.models.merchants_response_page import MerchantsResponsePage
from mercury_banking._runtime import ApiModel


class MerchantsResponse(ApiModel):
    """MerchantsResponse model."""

    data: List[MerchantInfo]
    page: MerchantsResponsePage
