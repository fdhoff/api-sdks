# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_needs_action_reason import BooksNeedsActionReason
from mercury_banking._runtime import ApiModel


class BooksAccrualSourceUnappliedPayment(ApiModel):
    """BooksAccrualSourceUnappliedPayment model."""

    amount: float
    needs_action_reason: BooksNeedsActionReason = Field(alias="needsActionReason")
