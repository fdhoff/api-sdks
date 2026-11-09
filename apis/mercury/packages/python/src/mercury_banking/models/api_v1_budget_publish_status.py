# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ApiV1BudgetPublishStatus(str, Enum):
    """Allowed values of ApiV1BudgetPublishStatus."""

    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
