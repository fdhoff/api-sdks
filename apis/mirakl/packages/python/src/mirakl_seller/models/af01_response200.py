# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.af01_response200_additional_fields import AF01Response200AdditionalFields
from mirakl_seller._runtime import ApiModel


class AF01Response200(ApiModel):
    """AF01Response200 model."""

    additional_fields: List[AF01Response200AdditionalFields]
    total_count: StrictInt
