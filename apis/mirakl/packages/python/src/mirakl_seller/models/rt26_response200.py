# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt26_response200_return_errors import RT26Response200ReturnErrors
from mirakl_seller.models.rt26_response200_return_success import RT26Response200ReturnSuccess
from mirakl_seller._runtime import ApiModel


class RT26Response200(ApiModel):
    """RT26Response200 model."""

    return_errors: Optional[List[RT26Response200ReturnErrors]] = None
    return_success: Optional[List[RT26Response200ReturnSuccess]] = None
