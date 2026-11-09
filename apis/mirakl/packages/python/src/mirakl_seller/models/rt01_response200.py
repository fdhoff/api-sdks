# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.rt01_response200_return_errors import RT01Response200ReturnErrors
from mirakl_seller.models.rt01_response200_return_success import RT01Response200ReturnSuccess
from mirakl_seller._runtime import ApiModel


class RT01Response200(ApiModel):
    """RT01Response200 model."""

    return_errors: List[RT01Response200ReturnErrors]
    return_success: List[RT01Response200ReturnSuccess]
