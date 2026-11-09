# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pm11_response200_attributes import PM11Response200Attributes
from mirakl_seller._runtime import ApiModel


class PM11Response200(ApiModel):
    """PM11Response200 model."""

    attributes: List[PM11Response200Attributes]
