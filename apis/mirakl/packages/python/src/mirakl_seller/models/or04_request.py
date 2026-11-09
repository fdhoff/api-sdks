# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or04_request_orders import OR04RequestOrders
from mirakl_seller._runtime import ApiModel


class OR04Request(ApiModel):
    """OR04Request model."""

    orders: Annotated[List[OR04RequestOrders], Field(min_length=1, max_length=100)]
