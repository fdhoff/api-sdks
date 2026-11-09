# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.of61_response200_offer_states import OF61Response200OfferStates
from mirakl_seller._runtime import ApiModel


class OF61Response200(ApiModel):
    """OF61Response200 model."""

    offer_states: List[OF61Response200OfferStates]
    total_count: StrictInt
