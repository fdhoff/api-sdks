# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st12_response200_data_fulfillment_center import ST12Response200DataFulfillmentCenter
from mirakl_seller._runtime import ApiModel


class ST12Response200DataFulfillment(ApiModel):
    """ST12Response200DataFulfillment model."""

    center: ST12Response200DataFulfillmentCenter
