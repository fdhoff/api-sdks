# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class CommitStatusState(str, Enum):
    """Allowed values of CommitStatusState."""

    PENDING = "pending"
    SUCCESS = "success"
    ERROR = "error"
    FAILURE = "failure"
    WARNING = "warning"
    SKIPPED = "skipped"
