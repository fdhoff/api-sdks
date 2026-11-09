# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.or11_response200_orders_customer_organization_address import (
    OR11Response200OrdersCustomerOrganizationAddress,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersCustomerOrganization(ApiModel):
    """OR11Response200OrdersCustomerOrganization model."""

    address: Optional[OR11Response200OrdersCustomerOrganizationAddress] = None
    electronic_address: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    identification_number: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    organization_id: Annotated[str, Field(strict=True, max_length=50)]
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    tax_identification_number: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
