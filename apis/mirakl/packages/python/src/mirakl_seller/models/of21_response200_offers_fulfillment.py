# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.of21_response200_offers_fulfillment_center import OF21Response200OffersFulfillmentCenter
from mirakl_seller._runtime import ApiModel


class OF21Response200OffersFulfillment(ApiModel):
    """OF21Response200OffersFulfillment model."""

    center: OF21Response200OffersFulfillmentCenter
