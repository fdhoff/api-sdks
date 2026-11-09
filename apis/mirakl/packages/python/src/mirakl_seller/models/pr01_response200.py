# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pr01_response200_promotions import PR01Response200Promotions
from mirakl_seller._runtime import ApiModel


class PR01Response200(ApiModel):
    """PR01Response200 model."""

    promotions: List[PR01Response200Promotions]
    total_count: StrictInt
