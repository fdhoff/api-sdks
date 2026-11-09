# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ApiSubscriptionTier(str, Enum):
    """Allowed values of ApiSubscriptionTier."""

    FREE = "free"
    PLUS = "plus"
    PREMIUM = "premium"
    PRO = "pro"
    ENTERPRISE = "enterprise"
