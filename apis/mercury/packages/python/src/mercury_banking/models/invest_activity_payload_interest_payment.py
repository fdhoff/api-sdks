# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.invest_activity_interest_payment import InvestActivityInterestPayment
from mercury_banking._runtime import ApiModel


class InvestActivityPayloadInterestPayment(ApiModel):
    """InvestActivityPayloadInterestPayment model."""

    contents: InvestActivityInterestPayment
    kind: StrictStr
