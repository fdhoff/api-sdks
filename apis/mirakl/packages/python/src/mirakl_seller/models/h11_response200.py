# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.h11_response200_hierarchies import H11Response200Hierarchies
from mirakl_seller._runtime import ApiModel


class H11Response200(ApiModel):
    """H11Response200 model."""

    hierarchies: List[H11Response200Hierarchies]
