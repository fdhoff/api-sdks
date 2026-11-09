# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.payment_method import PaymentMethod
from mercury_banking._runtime import ApiModel


class CreateRecipientInviteApiRequest(ApiModel):
    """CreateRecipientInviteApiRequest model."""

    contact_email: StrictStr = Field(alias="contactEmail")
    name: Optional[StrictStr] = None
    notes: Optional[StrictStr] = None
    organization_name_on_request: Optional[StrictStr] = Field(default=None, alias="organizationNameOnRequest")
    payment_methods: Annotated[List[PaymentMethod], Field(min_length=1)] = Field(alias="paymentMethods")
    recipient_id: Optional[UUID] = Field(default=None, alias="recipientId")
    require_tax_document: StrictBool = Field(alias="requireTaxDocument")
    send_email: StrictBool = Field(alias="sendEmail")
