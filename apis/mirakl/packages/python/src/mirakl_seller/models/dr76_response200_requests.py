# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr76_response200_requests_errors import DR76Response200RequestsErrors
from mirakl_seller.models.dr76_response200_requests_input import DR76Response200RequestsInput
from mirakl_seller._runtime import ApiModel


class DR76Response200Requests(ApiModel):
    """DR76Response200Requests model."""

    errors: Optional[List[DR76Response200RequestsErrors]] = None
    input: DR76Response200RequestsInput
