# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.invest_activity_status import InvestActivityStatus
from mercury_banking._runtime import ApiModel


class InvestActivityPortfolioChange(ApiModel):
    """InvestActivityPortfolioChange model."""

    var_from: StrictStr = Field(alias="from")
    status: InvestActivityStatus
    to: StrictStr
