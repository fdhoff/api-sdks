# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.m01_response200_messages import M01Response200Messages
from mirakl_seller._runtime import ApiModel


class M01Response200(ApiModel):
    """M01Response200 model."""

    messages: List[M01Response200Messages]
    total_count: StrictInt
