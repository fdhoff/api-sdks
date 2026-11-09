# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.api_safe_request_investor import APISafeRequestInvestor
from mercury_banking.models.api_safe_request_organization import APISafeRequestOrganization
from mercury_banking.models.us_state import USState
from mercury_banking.models.valuation_type import ValuationType
from mercury_banking._runtime import ApiModel


class APISafeRequest(ApiModel):
    """APISafeRequest model."""

    canceled_at: Optional[StrictStr] = Field(default=None, alias="canceledAt")
    discount_rate: Optional[Annotated[float, Field(multiple_of=0.01)]] = Field(default=None, alias="discountRate")
    document_url: StrictStr = Field(alias="documentUrl")
    expires_at: StrictStr = Field(alias="expiresAt")
    governing_state: Optional[USState] = Field(default=None, alias="governingState")
    id: UUID
    includes_most_favored_nation_clause: StrictBool = Field(alias="includesMostFavoredNationClause")
    includes_pro_rata_rights_letter: StrictBool = Field(alias="includesProRataRightsLetter")
    investment_amount: Annotated[float, Field(ge=0.01)] = Field(alias="investmentAmount")
    investment_date: date = Field(alias="investmentDate")
    investor: APISafeRequestInvestor
    organization: APISafeRequestOrganization
    paid_at: Optional[StrictStr] = Field(default=None, alias="paidAt")
    signed_by_investor_at: Optional[StrictStr] = Field(default=None, alias="signedByInvestorAt")
    signed_by_owner_at: Optional[StrictStr] = Field(default=None, alias="signedByOwnerAt")
    valuation_cap: Optional[Annotated[float, Field(ge=0.01)]] = Field(default=None, alias="valuationCap")
    valuation_type: ValuationType = Field(alias="valuationType")
