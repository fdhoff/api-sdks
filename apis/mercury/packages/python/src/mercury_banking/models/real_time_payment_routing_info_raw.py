# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.address_without_name import AddressWithoutName
from mercury_banking._runtime import ApiModel


class RealTimePaymentRoutingInfoRaw(ApiModel):
    """RealTimePaymentRoutingInfoRaw model."""

    account_number: StrictStr = Field(alias="accountNumber")
    address: AddressWithoutName
    routing_number: StrictStr = Field(alias="routingNumber")
