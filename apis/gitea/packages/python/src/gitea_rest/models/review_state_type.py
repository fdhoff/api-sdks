# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ReviewStateType(str, Enum):
    """Allowed values of ReviewStateType."""

    APPROVED = "APPROVED"
    PENDING = "PENDING"
    COMMENT = "COMMENT"
    REQUEST_CHANGES = "REQUEST_CHANGES"
    REQUEST_REVIEW = "REQUEST_REVIEW"
