# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or75_response200_taxes import OR75Response200Taxes
from mirakl_seller._runtime import ApiModel


class OR75Response200(ApiModel):
    """OR75Response200 model."""

    taxes: List[OR75Response200Taxes]
