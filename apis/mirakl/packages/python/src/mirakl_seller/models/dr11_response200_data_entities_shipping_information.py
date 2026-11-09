# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr11_response200_data_entities_shipping_information_ship_to_address import (
    DR11Response200DataEntitiesShippingInformationShipToAddress,
)
from mirakl_seller._runtime import ApiModel


class DR11Response200DataEntitiesShippingInformation(ApiModel):
    """DR11Response200DataEntitiesShippingInformation model."""

    ship_to_address: Optional[DR11Response200DataEntitiesShippingInformationShipToAddress] = None
