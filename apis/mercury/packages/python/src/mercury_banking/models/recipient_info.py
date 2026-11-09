# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.address import Address
from mercury_banking.models.address_without_name import AddressWithoutName
from mercury_banking.models.check_info import CheckInfo
from mercury_banking.models.domestic_wire_routing_info import DomesticWireRoutingInfo
from mercury_banking.models.electronic_routing_info import ElectronicRoutingInfo
from mercury_banking.models.international_wire_routing_info import InternationalWireRoutingInfo
from mercury_banking.models.payment_method import PaymentMethod
from mercury_banking.models.real_time_payment_routing_info import RealTimePaymentRoutingInfo
from mercury_banking.models.recipient_attachment import RecipientAttachment
from mercury_banking.models.recipient_status import RecipientStatus
from mercury_banking._runtime import ApiModel


class RecipientInfo(ApiModel):
    """RecipientInfo model."""

    address: Optional[Address] = None
    attachments: List[RecipientAttachment]
    check_info: Optional[CheckInfo] = Field(default=None, alias="checkInfo")
    contact_email: Optional[StrictStr] = Field(default=None, alias="contactEmail")
    date_last_paid: Optional[StrictStr] = Field(default=None, alias="dateLastPaid")
    default_address: Optional[AddressWithoutName] = Field(default=None, alias="defaultAddress")
    default_payment_method: PaymentMethod = Field(alias="defaultPaymentMethod")
    domestic_wire_routing_info: Optional[DomesticWireRoutingInfo] = Field(default=None, alias="domesticWireRoutingInfo")
    electronic_routing_info: Optional[ElectronicRoutingInfo] = Field(default=None, alias="electronicRoutingInfo")
    emails: List[StrictStr]
    id: UUID
    international_wire_routing_info: Optional[InternationalWireRoutingInfo] = Field(
        default=None, alias="internationalWireRoutingInfo"
    )
    invite_id: Optional[StrictStr] = Field(default=None, alias="inviteId")
    is_business: Optional[StrictBool] = Field(default=None, alias="isBusiness")
    name: StrictStr
    nickname: Optional[StrictStr] = None
    real_time_payment_routing_info: Optional[RealTimePaymentRoutingInfo] = Field(
        default=None, alias="realTimePaymentRoutingInfo"
    )
    status: RecipientStatus
