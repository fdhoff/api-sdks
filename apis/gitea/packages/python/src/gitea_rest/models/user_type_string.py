# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class UserTypeString(str, Enum):
    """Allowed values of UserTypeString."""

    USER = "User"
    ORGANIZATION = "Organization"
    BOT = "Bot"
