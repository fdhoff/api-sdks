# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ApiEventOperationType(str, Enum):
    """Allowed values of ApiEventOperationType."""

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
