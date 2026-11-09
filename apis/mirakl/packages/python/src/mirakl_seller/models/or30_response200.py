# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or30_response200_cancelations import OR30Response200Cancelations
from mirakl_seller._runtime import ApiModel


class OR30Response200(ApiModel):
    """OR30Response200 model."""

    cancelations: List[OR30Response200Cancelations]
    order_tax_mode: StrictStr
