# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.card import Card
from mercury_banking.models.card_list_response_page import CardListResponsePage
from mercury_banking._runtime import ApiModel


class CardListResponse(ApiModel):
    """CardListResponse model."""

    cards: List[Card]
    page: CardListResponsePage
