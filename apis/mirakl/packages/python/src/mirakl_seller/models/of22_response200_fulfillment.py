# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.of22_response200_fulfillment_center import OF22Response200FulfillmentCenter
from mirakl_seller._runtime import ApiModel


class OF22Response200Fulfillment(ApiModel):
    """OF22Response200Fulfillment model."""

    center: OF22Response200FulfillmentCenter
