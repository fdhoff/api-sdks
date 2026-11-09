# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt51_response200_return_label_errors import RT51Response200ReturnLabelErrors
from mirakl_seller.models.rt51_response200_return_label_successes import RT51Response200ReturnLabelSuccesses
from mirakl_seller._runtime import ApiModel


class RT51Response200(ApiModel):
    """RT51Response200 model."""

    return_label_errors: Optional[List[RT51Response200ReturnLabelErrors]] = None
    return_label_successes: Optional[List[RT51Response200ReturnLabelSuccesses]] = None
