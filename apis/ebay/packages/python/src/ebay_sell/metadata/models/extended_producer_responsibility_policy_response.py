# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.error import Error
from ebay_sell.metadata.models.extended_producer_responsibility_policy import ExtendedProducerResponsibilityPolicy
from ebay_sell._runtime import ApiModel


class ExtendedProducerResponsibilityPolicyResponse(ApiModel):
    """ExtendedProducerResponsibilityPolicyResponse model."""

    extended_producer_responsibilities: Optional[List[ExtendedProducerResponsibilityPolicy]] = Field(
        default=None, alias="extendedProducerResponsibilities"
    )
    warnings: Optional[List[Error]] = None
