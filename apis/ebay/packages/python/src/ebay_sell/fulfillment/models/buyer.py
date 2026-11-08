# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.extended_contact import ExtendedContact
from ebay_sell.fulfillment.models.tax_address import TaxAddress
from ebay_sell.fulfillment.models.tax_identifier import TaxIdentifier
from ebay_sell._runtime import ApiModel


class Buyer(ApiModel):
    """Buyer model."""

    buyer_registration_address: Optional[ExtendedContact] = Field(default=None, alias="buyerRegistrationAddress")
    tax_address: Optional[TaxAddress] = Field(default=None, alias="taxAddress")
    tax_identifier: Optional[TaxIdentifier] = Field(default=None, alias="taxIdentifier")
    username: Optional[StrictStr] = None
