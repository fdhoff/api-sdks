# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.api_billing_cadence import ApiBillingCadence
from mercury_banking.models.api_organization_kind import ApiOrganizationKind
from mercury_banking.models.api_subscription_tier import ApiSubscriptionTier
from mercury_banking.models.organization_dba import OrganizationDBA
from mercury_banking._runtime import ApiModel


class OrganizationInfo(ApiModel):
    """OrganizationInfo model."""

    billing_cadence: ApiBillingCadence = Field(alias="billingCadence")
    dbas: List[OrganizationDBA]
    ein: Optional[StrictStr] = None
    id: UUID
    kind: ApiOrganizationKind
    legal_business_name: StrictStr = Field(alias="legalBusinessName")
    subscription_tier: ApiSubscriptionTier = Field(alias="subscriptionTier")
