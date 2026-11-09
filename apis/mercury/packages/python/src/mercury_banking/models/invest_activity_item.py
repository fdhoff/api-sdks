# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.invest_activity_payload import InvestActivityPayload
from mercury_banking._runtime import ApiModel


class InvestActivityItem(ApiModel):
    """InvestActivityItem model."""

    day: date
    details: InvestActivityPayload
