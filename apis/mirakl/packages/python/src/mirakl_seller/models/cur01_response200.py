# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.cur01_response200_currencies import CUR01Response200Currencies
from mirakl_seller._runtime import ApiModel


class CUR01Response200(ApiModel):
    """CUR01Response200 model."""

    currencies: List[CUR01Response200Currencies]
