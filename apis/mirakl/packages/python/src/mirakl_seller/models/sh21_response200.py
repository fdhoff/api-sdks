# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.sh21_response200_carriers import SH21Response200Carriers
from mirakl_seller._runtime import ApiModel


class SH21Response200(ApiModel):
    """SH21Response200 model."""

    carriers: List[SH21Response200Carriers]
