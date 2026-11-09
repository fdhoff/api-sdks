# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.of21_response200_offers import OF21Response200Offers
from mirakl_seller._runtime import ApiModel


class OF21Response200(ApiModel):
    """OF21Response200 model."""

    offers: List[OF21Response200Offers]
    total_count: StrictInt
