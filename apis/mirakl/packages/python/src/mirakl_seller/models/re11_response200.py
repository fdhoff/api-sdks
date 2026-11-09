# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.re11_response200_reasons import RE11Response200Reasons
from mirakl_seller._runtime import ApiModel


class RE11Response200(ApiModel):
    """RE11Response200 model."""

    reasons: List[RE11Response200Reasons]
    total_count: StrictInt
