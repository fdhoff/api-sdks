# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class RT51RequestReturnLabelsLabelOptions(ApiModel):
    """RT51RequestReturnLabelsLabelOptions model."""

    qr_code: Optional[StrictBool] = None
