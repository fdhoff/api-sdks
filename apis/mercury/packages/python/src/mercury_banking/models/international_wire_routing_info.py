# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.address_without_name import AddressWithoutName
from mercury_banking.models.international_wire_correspondent_info import InternationalWireCorrespondentInfo
from mercury_banking.models.international_wire_country_specific_data import InternationalWireCountrySpecificData
from mercury_banking.models.swift_code_data import SwiftCodeData
from mercury_banking._runtime import ApiModel


class InternationalWireRoutingInfo(ApiModel):
    """InternationalWireRoutingInfo model."""

    address: Optional[AddressWithoutName] = None
    bank_details: Optional[SwiftCodeData] = Field(default=None, alias="bankDetails")
    correspondent_info: Optional[InternationalWireCorrespondentInfo] = Field(default=None, alias="correspondentInfo")
    country_specific: InternationalWireCountrySpecificData = Field(alias="countrySpecific")
    email_address: Optional[StrictStr] = Field(default=None, alias="emailAddress")
    iban: StrictStr
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    swift_code: StrictStr = Field(alias="swiftCode")
