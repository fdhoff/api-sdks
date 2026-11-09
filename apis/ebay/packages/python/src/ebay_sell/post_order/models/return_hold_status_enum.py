# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ReturnHoldStatusEnum(str, Enum):
    """Allowed values of ReturnHoldStatusEnum."""

    HOLD_CREATION_SUCCESS = "HOLD_CREATION_SUCCESS"
    HOLD_RELEASE_SUCCESS = "HOLD_RELEASE_SUCCESS"
    HOLD_RELEASE_FAILED = "HOLD_RELEASE_FAILED"
    INELIGIBLE_TO_RELEASE_HOLD = "INELIGIBLE_TO_RELEASE_HOLD"
    OTHER = "OTHER"
