# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.address_data import AddressData
from mercury_banking.models.credit_card_info import CreditCardInfo
from mercury_banking.models.debit_card_info import DebitCardInfo
from mercury_banking.models.domestic_wire_routing_info import DomesticWireRoutingInfo
from mercury_banking.models.electronic_routing_info import ElectronicRoutingInfo
from mercury_banking.models.international_wire_routing_info import InternationalWireRoutingInfo
from mercury_banking._runtime import ApiModel


class TransactionMethodData(ApiModel):
    """TransactionMethodData model."""

    address: Optional[AddressData] = None
    credit_card_info: Optional[CreditCardInfo] = Field(default=None, alias="creditCardInfo")
    debit_card_info: Optional[DebitCardInfo] = Field(default=None, alias="debitCardInfo")
    domestic_wire_routing_info: Optional[DomesticWireRoutingInfo] = Field(default=None, alias="domesticWireRoutingInfo")
    electronic_routing_info: Optional[ElectronicRoutingInfo] = Field(default=None, alias="electronicRoutingInfo")
    international_wire_routing_info: Optional[InternationalWireRoutingInfo] = Field(
        default=None, alias="internationalWireRoutingInfo"
    )
