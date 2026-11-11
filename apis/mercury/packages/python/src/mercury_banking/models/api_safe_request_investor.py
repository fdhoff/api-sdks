# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.safe_request_investor_type import SafeRequestInvestorType
from mercury_banking._runtime import ApiModel


class APISafeRequestInvestor(ApiModel):
    """APISafeRequestInvestor model."""

    additional_bylines: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=299)]] = Field(
        default=None, alias="additionalBylines"
    )
    address: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=299)]] = None
    investor_type: SafeRequestInvestorType = Field(alias="investorType")
    legal_entity_name: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="legalEntityName")
    signatory_email: StrictStr = Field(alias="signatoryEmail")
    signatory_name: Annotated[str, Field(min_length=1, strict=True, max_length=5000)] = Field(alias="signatoryName")
    signatory_title: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=299)]] = Field(
        default=None, alias="signatoryTitle"
    )
