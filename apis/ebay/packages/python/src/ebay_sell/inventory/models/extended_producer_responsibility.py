# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.amount import Amount
from ebay_sell._runtime import ApiModel


class ExtendedProducerResponsibility(ApiModel):
    """ExtendedProducerResponsibility model."""

    eco_participation_fee: Optional[Amount] = Field(default=None, alias="ecoParticipationFee")
    producer_product_id: Optional[StrictStr] = Field(default=None, alias="producerProductId")
    product_documentation_id: Optional[StrictStr] = Field(default=None, alias="productDocumentationId")
    product_package_id: Optional[StrictStr] = Field(default=None, alias="productPackageId")
    shipment_package_id: Optional[StrictStr] = Field(default=None, alias="shipmentPackageId")
