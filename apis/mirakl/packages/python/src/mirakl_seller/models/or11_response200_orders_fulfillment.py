# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or11_response200_orders_fulfillment_center import OR11Response200OrdersFulfillmentCenter
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersFulfillment(ApiModel):
    """OR11Response200OrdersFulfillment model."""

    center: OR11Response200OrdersFulfillmentCenter
