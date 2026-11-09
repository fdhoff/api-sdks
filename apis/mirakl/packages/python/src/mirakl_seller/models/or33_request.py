# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or33_request_order_lines import OR33RequestOrderLines
from mirakl_seller._runtime import ApiModel


class OR33Request(ApiModel):
    """OR33Request model."""

    order_lines: Annotated[List[OR33RequestOrderLines], Field(min_length=1, max_length=100)]
