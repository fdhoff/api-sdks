# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ApiV1BudgetFrequency(str, Enum):
    """Allowed values of ApiV1BudgetFrequency."""

    ONETIME = "oneTime"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
