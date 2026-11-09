# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.or15_response200_ext_file_structure_orders_customer_organization_address import (
    OR15Response200ExtFileStructureOrdersCustomerOrganizationAddress,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersCustomerOrganization(ApiModel):
    """OR15Response200ExtFileStructureOrdersCustomerOrganization model."""

    address: Optional[OR15Response200ExtFileStructureOrdersCustomerOrganizationAddress] = None
    electronic_address: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    identification_number: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    organization_id: Annotated[str, Field(strict=True, max_length=50)]
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    tax_identification_number: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
