# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.address_data import AddressData
from mercury_banking.models.check_info_raw import CheckInfoRaw
from mercury_banking.models.domestic_wire_routing_info_raw import DomesticWireRoutingInfoRaw
from mercury_banking.models.electronic_routing_info_raw import ElectronicRoutingInfoRaw
from mercury_banking.models.real_time_payment_routing_info_raw import RealTimePaymentRoutingInfoRaw
from mercury_banking._runtime import ApiModel


class EditRecipientRequest(ApiModel):
    """EditRecipientRequest model."""

    address: Optional[AddressData] = None
    check_info: Optional[CheckInfoRaw] = Field(default=None, alias="checkInfo")
    contact_email: Optional[StrictStr] = Field(default=None, alias="contactEmail")
    domestic_wire_routing_info: Optional[DomesticWireRoutingInfoRaw] = Field(
        default=None, alias="domesticWireRoutingInfo"
    )
    electronic_routing_info: Optional[ElectronicRoutingInfoRaw] = Field(default=None, alias="electronicRoutingInfo")
    emails: Optional[List[StrictStr]] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=299)]] = None
    nickname: Optional[StrictStr] = None
    real_time_payment_routing_info: Optional[RealTimePaymentRoutingInfoRaw] = Field(
        default=None, alias="realTimePaymentRoutingInfo"
    )
