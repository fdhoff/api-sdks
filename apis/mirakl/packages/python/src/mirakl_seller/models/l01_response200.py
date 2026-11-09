# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.l01_response200_locales import L01Response200Locales
from mirakl_seller._runtime import ApiModel


class L01Response200(ApiModel):
    """L01Response200 model."""

    locales: List[L01Response200Locales]
