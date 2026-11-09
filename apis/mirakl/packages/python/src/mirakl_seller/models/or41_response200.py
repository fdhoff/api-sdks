# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or41_response200_messages import OR41Response200Messages
from mirakl_seller._runtime import ApiModel


class OR41Response200(ApiModel):
    """OR41Response200 model."""

    messages: List[OR41Response200Messages]
    total_count: StrictInt
