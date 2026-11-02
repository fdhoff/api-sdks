# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BuybackKycDocuments(str, Enum):
    """Allowed values of BuybackKycDocuments."""

    PASSPORT = "PASSPORT"
    ID = "ID"
    ID_CARD_FRONT = "ID_CARD_FRONT"
    ID_CARD_BACK = "ID_CARD_BACK"
    BANK_STATEMENT = "BANK_STATEMENT"
    DRIVING_LICENCE_FRONT = "DRIVING_LICENCE_FRONT"
    DRIVING_LICENCE_BACK = "DRIVING_LICENCE_BACK"
